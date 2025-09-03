import easyocr

reader = easyocr.Reader(['en'])

img_path = '/Users/santiagovargas/Desktop/Vision2Summary/backend/ocr/test2.jpeg'
result = reader.readtext(img_path)

print("\n--- Detected Text ---")
for (bbox, text, prob) in result:
    print(text)