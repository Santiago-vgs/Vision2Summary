import pytesseract
import cv2

from preprocessing import binarisation
from preprocessing import noise_removal


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

    # 2. Apply noise removal to the *output* of the binarisation step.
    # The 'noise_removal' function should return the denoised NumPy array.
    #final_processed_image = noise_removal(gray_image)

    # 3. Run OCR on the final processed NumPy array.
    # pytesseract.image_to_string can often handle NumPy arrays directly.


   ##### extracted_text = pytesseract.image_to_string(final_processed_image)

    ####### TESTING BINARISATION ######

    extracted_text = pytesseract.image_to_string(gray_image)

    print("--- Extracted Text ---")
    print(extracted_text)
    
