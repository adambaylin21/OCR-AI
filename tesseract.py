import pytesseract
from PIL import Image

import sys

def snapImage001(image):
    """
    Extracts text from an image using OCR.

    :param image_path: Path to the image file
    :return: Extracted text as a string
    """
    try:
        # Open the image using PIL
        # image = Image.open(image_path)

        # Use pytesseract to perform OCR on the image
        text = pytesseract.image_to_string(image, lang='fra')

        return text
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    if len(sys.argv) != 2:
        print("Sử dụng: python script.py <tên_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    print(f"File nhận được: {file_path}")

    # Code xử lý file ở đây


if __name__ == "__main__":
    # main()
    # Path to the image file
    # image_path = "/Volumes/Extend/Find Idea/img/1042 - 100000092604293_9463826760296983 - 2390.jpg"

    # Extract text from the image
    # extracted_text = snapImage001(image_path)

    # Print the extracted text
    # print(extracted_text)

    pass