import cv2
import numpy as np
from PIL import Image

# Convert the image to grayscale and save it
def binarisation(Image):
    gray_image = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("grayscale_test.jpeg", gray_image)
    return gray_image

def noise_removal(Image):
    kernel = np.ones((1,1), np.uint8)
    denoised_image = cv2.morphologyEx(Image, cv2.MORPH_CLOSE, kernel)
    denoised_image = cv2.medianBlur(Image, 3)

    cv2.imwrite("noise_remove_test.jpeg", denoised_image)
    return denoised_image

def upscaling(Image):
    up_width = 1100
    up_height = 800
    up_points = (up_width, up_height)
    resised_up = cv2.resize(Image, up_points, interpolation= cv2.INTER_LINEAR)
    
    cv2.imwrite("upscaled_test.jpeg", resised_up)
    return resised_up

def sharpness(Image):
    blurred = cv2.GaussianBlur(Image, (0, 0), 3)
    sharpened_image = cv2.addWeighted(Image, 1.5, blurred, -0.5, 0)

    cv2.imwrite("sharpened_test.jpeg", sharpened_image)
    return sharpened_image

    
    




