import PIL.Image
import cv2
import pytesseract


def main():
    test_image_processing()

def test_image_processing():
    image = cv2.imread('img.png')
    text = pytesseract.image_to_string(image)
    print(text)





main()
