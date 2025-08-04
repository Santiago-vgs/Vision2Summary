import cv2

# Convert the image to grayscale and save it
def binarisation(Image):
    gray_image = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("grayscale_test.jpeg", gray_image)
    return gray_image




