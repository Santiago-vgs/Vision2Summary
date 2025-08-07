import cv2
import numpy as np
from PIL import Image

# Convert the image to grayscale and save it
def binarisation(Image):
    gray_image = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("grayscale_test.jpeg", gray_image)
    return gray_image

def noise_removal(Image):
    kernel = np.ones((2,2), np.uint8)
    denoised_image = cv2.morphologyEx(Image, cv2.MORPH_CLOSE, kernel)
    denoised_image = cv2.medianBlur(Image, 3)

    cv2.imwrite("noise_remove_test.jpeg", denoised_image)
    return denoised_image

def scaling(Image):

    
    




