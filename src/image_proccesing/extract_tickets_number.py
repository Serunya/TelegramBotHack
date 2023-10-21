
import cv2
from pyzbar import pyzbar

def main():
    __extractNumFromImage()

def __extractNumFromPdf():
    pass

def __extractNumFromImage():
    pass

def __extractNumForImage(pil_image):
   pass



def __isPasport(image):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    if len(faces) > 0:
        return True
    else:
        return False


main()
