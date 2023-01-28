import cv2
import numpy as np
from keras.models import load_model
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array
import numpy as np
import requests
from keras.models import load_model
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def urloimg(urltoimg):
    response = requests.get(urltoimg)
    open('temp.jpg', 'wb').write(response.content)

def predictimg(imagecuy):
    imageee = urloimg(imagecuy)
    model = load_model('./model_saved.h5')
    image = load_img('./temp.jpg', target_size=(224, 224))
    img = np.array(image)
    img = img / 255.0
    img = np.reshape(image, (1, 224, 224, 3))
    label = model.predict(img)
    if round(label[0][0]) == 1:
        return("Car")
    elif round(label[0][0]) == 0:
        return("Plane")
    else:
        return("Nothing found")

def imgttxt(imageeeee, languaggee="eng"):
    imagekh = urloimg(imageeeee)
    image = cv2.imread('./temp.jpg')
    # convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # apply thresholding to preprocess the image
    threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # recognize the text in the image using Tesseract OCR
    text = pytesseract.image_to_string(threshold, lang=languaggee)
    return(text)
def getToken():
    return("Your Token")
