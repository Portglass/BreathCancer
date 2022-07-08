## Making essential imports
import numpy as np
import matplotlib.pyplot as plt
import cv2
from tensorflow.keras.models import load_model
import matplotlib.image as mpimg

class model:
     def __init__(self,path):
          self.model = load_model(path)

     def predict(self,pathImg, shape=256):
          img = mpimg.imread(pathImg)
          img = cv2.resize(img, (shape, shape))
          imgProc = np.array([img])
          predictions = self.model.predict(imgProc)
          return predictions[0], imgProc[0]

