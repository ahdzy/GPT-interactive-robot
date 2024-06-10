import easyocr

def extract_text_from_image(image_path):
    # Create an OCR reader
    reader = easyocr.Reader(['en'])  # Specify the language(s) you want to support

    # Read text from the image
    result = reader.readtext(image_path)

    # Extracted text is in the 'text' field of each result
    extracted_text = [item[1] for item in result]

    return extracted_text