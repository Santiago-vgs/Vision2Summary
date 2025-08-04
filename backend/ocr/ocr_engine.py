import pytesseract
import cv2

from preprocessing import binarisation


image_path = "/Users/santiagovargas/Desktop/Vision2Summary/backend/ocr/test2.jpeg"

# Load the image with OpenCV
image = cv2.imread(image_path)

# Call the function to process the image and save the result
gray_image = binarisation(image)

# Run OCR on the grayscale image and print the result
extracted_text = pytesseract.image_to_string(gray_image)

print("--- Extracted Text ---")
print(extracted_text)
print("----------------------")

print("Saved grayscale image as: grayscale_test.jpeg")
