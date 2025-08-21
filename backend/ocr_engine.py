import pytesseract
import cv2

from preprocessing import binarisation
from preprocessing import noise_removal
from preprocessing import upscaling
from preprocessing import sharpness


image_path = "/Users/santiagovargas/Desktop/Vision2Summary/backend/ocr/test2.jpeg"

# Load the image with OpenCV
image = cv2.imread(image_path)

# Add a check to ensure the image loaded successfully
if image is None:
    print(f"Error: Could not load image from {image_path}. Please check the path.")
else:
    # 1. Apply binarisation. This function should return a grayscale NumPy array.
    # It also saves 'grayscale_test.jpeg' internally.
    gray_image = binarisation(image)

   ##### extracted_text = pytesseract.image_to_string(final_processed_image)

   ### TESTING UP SCLAING #####
    upscaled_image = upscaling(gray_image)

    ####### TESTING SHARPNESS #######
    final_processed_image = sharpness(upscaled_image)


   ##### OUTPUT ########
    extracted_text = pytesseract.image_to_string(final_processed_image)

    print("--- Extracted Text ---") 
    print(extracted_text)
    
