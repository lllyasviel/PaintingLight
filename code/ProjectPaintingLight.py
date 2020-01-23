# Project PaintingLight V 0.1
# Team of Style2Paints 2020
# Non-commercial usage only


import cv2
import rtree
import scipy
import trimesh
import numpy as np
import tensorflow as tf
from scipy.spatial import ConvexHull
from cv2.ximgproc import createGuidedFilter


assert tf.__version__ == '1.12.0'
assert scipy.__version__ == '1.3.2'
assert trimesh.__version__ == '2.37.1'
assert rtree.__version__ == '0.9.3'


# We use SR-CNN as pre-processing to remove JPEG artifacts in input images.
# You can remove these code if you have high-quality PNG images.

def get_session(gpu_fraction=0.3):
    gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=gpu_fraction, allow_growth=True)
    return tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))


session = get_session()
tf.keras.backend.set_session(session)
ip3 = tf.placeholder(dtype=tf.float32, shape=(None, None, None, 3))
srcnn = tf.keras.models.load_model('srcnn.net')
srcnn_op = srcnn(tf.pad(ip3 / 255.0, [[0, 0], [16, 16], [16, 16], [0, 0]], 'REFLECT'))[:, 16:-16, 16:-16, :] * 255.0
session.run(tf.global_variables_initializer())
srcnn.load_weights('srcnn.net')


# Global position of light source.
gx = 0.0
gy = 0.0


def run_srcnn(x):
    return session.run(srcnn_op, feed_dict={ip3: x[None, :, :, :]})[0].clip(0, 255).astype(np.uint8)


# Some image resizing tricks.
def min_resize(x, m):
    if x.shape[0] < x.shape[1]:
        s0 = m
        s1 = int(float(m) / float(x.shape[0]) * float(x.shape[1]))
    else:
        s0 = int(float(m) / float(x.shape[1]) * float(x.shape[0]))
        s1 = m
    new_max = min(s1, s0)
    raw_max = min(x.shape[0], x.shape[1])
    if new_max < raw_max:
        interpolation = cv2.INTER_AREA
    else:
        interpolation = cv2.INTER_LANCZOS4
    y = cv2.resize(x, (s1, s0), interpolation=interpolation)
    return y


# Some image resizing tricks.
def d_resize(x, d, fac=1.0):
    new_min = min(int(d[1] * fac), int(d[0] * fac))
    raw_min = min(x.shape[0], x.shape[1])
    if new_min < raw_min:
        interpolation = cv2.INTER_AREA
    else:
        interpolation = cv2.INTER_LANCZOS4
    y = cv2.resize(x, (int(d[1] * fac), int(d[0] * fac)), interpolation=interpolation)
    return y


# Some image gradient computing tricks.
def get_image_gradient(dist):
    cols = cv2.filter2D(dist, cv2.CV_32F, np.array([[-1, 0, +1], [-2, 0, +2], [-1, 0, +1]]))
    rows = cv2.filter2D(dist, cv2.CV_32F, np.array([[-1, -2, -1], [0, 0, 0], [+1, +2, +1]]))
    return cols, rows


def generate_lighting_effects(stroke_density, content):

    # Computing the coarse lighting effects
    # In original paper we compute the coarse effects using Gaussian filters.
    # Here we use a Gaussian pyramid to get similar results.
    # This pyramid-based result is a bit better than naive filters.
    h512 = content
    h256 = cv2.pyrDown(h512)
    h128 = cv2.pyrDown(h256)
    h64 = cv2.pyrDown(h128)
    h32 = cv2.pyrDown(h64)
    h16 = cv2.pyrDown(h32)
    c512, r512 = get_image_gradient(h512)
    c256, r256 = get_image_gradient(h256)
    c128, r128 = get_image_gradient(h128)
    c64, r64 = get_image_gradient(h64)
    c32, r32 = get_image_gradient(h32)
    c16, r16 = get_image_gradient(h16)
    c = c16
    c = d_resize(cv2.pyrUp(c), c32.shape) * 4.0 + c32
    c = d_resize(cv2.pyrUp(c), c64.shape) * 4.0 + c64
    c = d_resize(cv2.pyrUp(c), c128.shape) * 4.0 + c128
    c = d_resize(cv2.pyrUp(c), c256.shape) * 4.0 + c256
    c = d_resize(cv2.pyrUp(c), c512.shape) * 4.0 + c512
    r = r16
    r = d_resize(cv2.pyrUp(r), r32.shape) * 4.0 + r32
    r = d_resize(cv2.pyrUp(r), r64.shape) * 4.0 + r64
    r = d_resize(cv2.pyrUp(r), r128.shape) * 4.0 + r128
    r = d_resize(cv2.pyrUp(r), r256.shape) * 4.0 + r256
    r = d_resize(cv2.pyrUp(r), r512.shape) * 4.0 + r512
    coarse_effect_cols = c
    coarse_effect_rows = r

    # Normalization
    EPS = 1e-10
    max_effect = np.max((coarse_effect_cols**2 + coarse_effect_rows**2)**0.5)
    coarse_effect_cols = (coarse_effect_cols + EPS) / (max_effect + EPS)
    coarse_effect_rows = (coarse_effect_rows + EPS) / (max_effect + EPS)

    # Refinement
    stroke_density_scaled = (stroke_density.astype(np.float32) / 255.0).clip(0, 1)
    coarse_effect_cols *= (1.0 - stroke_density_scaled ** 2.0 + 1e-10) ** 0.5
    coarse_effect_rows *= (1.0 - stroke_density_scaled ** 2.0 + 1e-10) ** 0.5
    refined_result = np.stack([stroke_density_scaled, coarse_effect_rows, coarse_effect_cols], axis=2)

    return refined_result


def run(image, mask, ambient_intensity, light_intensity, light_source_height, gamma_correction, stroke_density_clipping, light_color_red, light_color_green, light_color_blue, enabling_multiple_channel_effects):

    # Some pre-processing to resize images and remove input JPEG artifacts.
    raw_image = min_resize(image, 512)
    raw_image = run_srcnn(raw_image)
    raw_image = min_resize(raw_image, 512)
    raw_image = raw_image.astype(np.float32)
    unmasked_image = raw_image.copy()

    if mask is not None:
        alpha = np.mean(d_resize(mask, raw_image.shape).astype(np.float32) / 255.0, axis=2, keepdims=True)
        raw_image = unmasked_image * alpha

    # Compute the convex-hull-like palette.
    h, w, c = raw_image.shape
    flattened_raw_image = raw_image.reshape((h * w, c))
    raw_image_center = np.mean(flattened_raw_image, axis=0)
    hull = ConvexHull(flattened_raw_image)

    # Estimate the stroke density map.
    intersector = trimesh.Trimesh(faces=hull.simplices, vertices=hull.points).ray
    start = np.tile(raw_image_center[None, :], [h * w, 1])
    direction = flattened_raw_image - start
    print('Begin ray intersecting ...')
    index_tri, index_ray, locations = intersector.intersects_id(start, direction, return_locations=True, multiple_hits=True)
    print('Intersecting finished.')
    intersections = np.zeros(shape=(h * w, c), dtype=np.float32)
    intersection_count = np.zeros(shape=(h * w, 1), dtype=np.float32)
    CI = index_ray.shape[0]
    for c in range(CI):
        i = index_ray[c]
        intersection_count[i] += 1
        intersections[i] += locations[c]
    intersections = (intersections + 1e-10) / (intersection_count + 1e-10)
    intersections = intersections.reshape((h, w, 3))
    intersection_count = intersection_count.reshape((h, w))
    intersections[intersection_count < 1] = raw_image[intersection_count < 1]
    intersection_distance = np.sqrt(np.sum(np.square(intersections - raw_image_center[None, None, :]), axis=2, keepdims=True))
    pixel_distance = np.sqrt(np.sum(np.square(raw_image - raw_image_center[None, None, :]), axis=2, keepdims=True))
    stroke_density = ((1.0 - np.abs(1.0 - pixel_distance / intersection_distance)) * stroke_density_clipping).clip(0, 1) * 255

    # A trick to improve the quality of the stroke density map.
    # It uses guided filter to remove some possible artifacts.
    # You can remove these codes if you like sharper effects.
    guided_filter = createGuidedFilter(pixel_distance.clip(0, 255).astype(np.uint8), 1, 0.01)
    for _ in range(4):
        stroke_density = guided_filter.filter(stroke_density)

    # Visualize the estimated stroke density.
    cv2.imwrite('stroke_density.png', stroke_density.clip(0, 255).astype(np.uint8))

    # Then generate the lighting effects
    raw_image = unmasked_image.copy()
    lighting_effect = np.stack([
        generate_lighting_effects(stroke_density, raw_image[:, :, 0]),
        generate_lighting_effects(stroke_density, raw_image[:, :, 1]),
        generate_lighting_effects(stroke_density, raw_image[:, :, 2])
    ], axis=2)

    # Using a simple user interface to display results.

    def update_mouse(event, x, y, flags, param):
        global gx
        global gy
        gx = - float(x % w) / float(w) * 2.0 + 1.0
        gy = - float(y % h) / float(h) * 2.0 + 1.0
        return

    light_source_color = np.array([light_color_blue, light_color_green, light_color_red])

    global gx
    global gy

    while True:
        light_source_location = np.array([[[light_source_height, gy, gx]]], dtype=np.float32)
        light_source_direction = light_source_location / np.sqrt(np.sum(np.square(light_source_location)))
        final_effect = np.sum(lighting_effect * light_source_direction, axis=3).clip(0, 1)
        if not enabling_multiple_channel_effects:
            final_effect = np.mean(final_effect, axis=2, keepdims=True)
        rendered_image = (ambient_intensity + final_effect * light_intensity) * light_source_color * raw_image
        rendered_image = ((rendered_image / 255.0) ** gamma_correction) * 255.0
        canvas = np.concatenate([raw_image, rendered_image], axis=1).clip(0, 255).astype(np.uint8)
        cv2.imshow('Move your mouse on the canvas to play!', canvas)
        cv2.setMouseCallback('Move your mouse on the canvas to play!', update_mouse)
        cv2.waitKey(10)
