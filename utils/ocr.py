# ocr.py improvements
import easyocr
import pytesseract
from PIL import Image
import pdf2image

def perform_ocr(filepath):
    # Handle PDFs by converting to images
    if filepath.lower().endswith('.pdf'):
        images = pdf2image.convert_from_path(filepath)
        text = ""
        for image in images:
            text += pytesseract.image_to_string(image) + "\n"
        return text.strip()
    
    # Use both EasyOCR and Tesseract for better accuracy
    try:
        # EasyOCR
        reader = easyocr.Reader(['en'], gpu=True)  # Enable GPU if available
        easy_result = " ".join(reader.readtext(filepath, detail=0))
        
        # Tesseract
        tess_result = pytesseract.image_to_string(Image.open(filepath))
        
        # Combine results for better accuracy
        return combine_ocr_results(easy_result, tess_result)
    except Exception as e:
        print(f"OCR Error: {e}")
        return ""

def combine_ocr_results(text1, text2):
    # Simple combination - can be enhanced with more sophisticated merging
    if len(text1) > len(text2):
        return text1
    return text2