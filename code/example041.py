import cv2

image = cv2.imread('./imgs/041.jpg')
mask = None

ambient_intensity = 0.55
light_intensity = 0.9
light_source_height = 1.0
gamma_correction = 1.3
stroke_density_clipping = 1.2
enabling_multiple_channel_effects = True

light_color_red = 1.0
light_color_green = 0.83
light_color_blue = 0.58


from ProjectPaintingLight import run


run(image, mask, ambient_intensity, light_intensity, light_source_height,
    gamma_correction, stroke_density_clipping, light_color_red, light_color_green,
    light_color_blue, enabling_multiple_channel_effects)
    
