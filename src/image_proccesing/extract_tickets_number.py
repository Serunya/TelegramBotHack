import PIL.Image
import cv2
import pytesseract
from pdf417decoder import PDF417Decoder
from pyzbar import pyzbar
import numpy as np
import re
from glob import glob


def main():
    getTicketNumber()


def getTicketNumber():
    image = cv2.imread("img_1.png")
    print(__extractNumFromImage(image))


def __getBarcode(gray):
    gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
    gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)
    gradient = cv2.subtract(gradX, gradY)
    gradient = cv2.convertScaleAbs(gradient)
    blurred = cv2.GaussianBlur(gradient, (9, 9), 0)
    (_, thresh) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    closed = cv2.erode(closed, None, iterations=4)
    closed = cv2.dilate(closed, None, iterations=4)
    contours, _ = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    rectangles = []

    for c in contours:
        rect = cv2.minAreaRect(c)
        box = np.intp(cv2.boxPoints(rect))
        rectangles.append(box)
    for i, rect in enumerate(rectangles):
        x, y, w, h = cv2.boundingRect(rect)
        x -= 50
        y -= 50
        w += 100
        h += 100
        barcode_area = gray[y:y + h, x:x + w]
        if barcode_area is not None and not np.all(barcode_area == 0):
            barcodes = pyzbar.decode(barcode_area)
            if barcodes:
                return barcodes[0].data.decode('utf-8')
    return None


def __getTicketNumFromImage(gray_image):
    scale_percent = int(350)  # Процент от изначального размера
    width = int(gray_image.shape[1] * scale_percent / 100)
    height = int(gray_image.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(gray_image, dim, interpolation=cv2.INTER_AREA)
    ret, threshold_image = cv2.threshold(resized, 210, 200, 1, cv2.THRESH_BINARY)
    cv2.imwrite("dsa2.png",resized)
    cv2.imwrite("dsa2.png", threshold_image)
    text = pytesseract.image_to_string(threshold_image, config='--psm 11').replace(" ","")
    pattern = r'\d{14}'
    matches = re.findall(pattern, text)
    for match in matches:
        return match


def __extractNumFromImage(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    barcode = __getBarcode(gray)
    if(barcode == None):
        return __getTicketNumFromImage(gray)
    else:
        return barcode + "sd"


def __isPasport(image):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    if len(faces) > 0:
        return True
    else:
        return False


main()
