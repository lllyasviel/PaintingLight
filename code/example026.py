import cv2

image = cv2.imread('./imgs/026.jpg')
mask = None

ambient_intensity = 0.4
light_intensity = 1.2
light_source_height = 0.618
gamma_correction = 1.0
stroke_density_clipping = 1.0
enabling_multiple_channel_effects = True

light_color_red = 1.0
light_color_green = 1.0
light_color_blue = 1.0


from ProjectPaintingLight import run


run(image, mask, ambient_intensity, light_intensity, light_source_height,
    gamma_correction, stroke_density_clipping, light_color_red, light_color_green,
    light_color_blue, enabling_multiple_channel_effects)
    
