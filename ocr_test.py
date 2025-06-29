from PIL import Image
import pytesseract

# ✅ Correct path based on your setup
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = Image.open("uploads/test.jpg")  # ya test.png
text = pytesseract.image_to_string(img)

print("✅ OCR Result:", text)
