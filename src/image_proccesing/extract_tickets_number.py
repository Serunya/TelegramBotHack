import PIL.Image
import cv2
import pytesseract


def main():
    test_image_processing()

def test_image_processing():
    image = PIL.Image.open('img2.jpg')
    text = pytesseract.image_to_string(image)
    print(text)


main()
