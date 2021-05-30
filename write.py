import cv2

import pytesseract

def convert(path):
	img=cv2.imread(path)
	text=pytesseract.image_to_string(img)
	return text
