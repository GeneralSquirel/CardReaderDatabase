import cv2
from pytesseract import pytesseract 
from PIL import Image

camera=cv2.VideoCapture(0)

if not (camera.isOpened()):
	print("Could not open video device")

while True:
	_,Imagee = camera.read()
	cv2.imshow("kaart", Imagee)
	if cv2.waitKey(1) & 0xFF==ord("s"):
		cv2.imwrite("kaart.png", Imagee)
		break
camera.release()
cv2.destroyAllWindows()

def tesseract():
	imagepath="kaart.png"
	text=pytesseract.image_to_string(Image.open(imagepath))
	print(text)
tesseract()
	

