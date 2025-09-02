import pytesseract
from PIL import Image, ImageDraw, ImageFont

# (Windows only) Set the path to Tesseract if not already in PATH
# Uncomment and edit if needed:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def test_pytesseract():
    print("Checking pytesseract installation...")

    try:
        # Print installed Tesseract version
        version = pytesseract.get_tesseract_version()
        print(f"[OK] Tesseract version: {version}")
    except Exception as e:
        print(f"[ERROR] Cannot find Tesseract OCR engine: {e}")
        return

    # Create a sample image with text
    img = Image.new("RGB", (300, 100), color="white")
    draw = ImageDraw.Draw(img)
    draw.text((10, 40), "Hello OCR", fill="black")

    # Save image for reference
    img.save("sample_test.png")

    # Run OCR on the sample image
    try:
        extracted_text = pytesseract.image_to_string(img)
        print("[INFO] OCR Extracted Text:", repr(extracted_text.strip()))
    except Exception as e:
        print(f"[ERROR] OCR failed: {e}")
        return

    # Final result
    if "Hello" in extracted_text:
        print("[SUCCESS] pytesseract is working correctly ✅")
    else:
        print("[WARNING] pytesseract did not read text correctly ⚠️")

if __name__ == "__main__":
    test_pytesseract()
