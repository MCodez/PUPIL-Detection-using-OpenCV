# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 12:46:13 2019
IDE : Anaconda (Spyder)
@author: LALIT ARORA
"""

import cv2
import os
import numpy as np


class iris_detection():
    def __init__(self, image_path):
        self._img = None
        self._img_path = image_path
        self._pupil = None

    def load_image(self):
        self._img = cv2.imread(self._img_path)
        # If the image doesn't exists or is not valid then imread returns None
        if type(self._img) == None:
            return False
        else:
            return True
        
    def save_image (self):
        name = "\\".join(self._img_path.split('\\')[:-1])+"\\result_erosion\\"+str(self._img_path.split('\\')[-1])+".jpg"
        print(name)
        cv2.imwrite(name,self._img)
        
    def detect_iris (self):
        inv = cv2.bitwise_not(self._img)
        thresh = cv2.cvtColor(inv, cv2.COLOR_BGR2GRAY)
        kernel = np.ones((2,2),np.uint8)
        erosion = cv2.erode(thresh,kernel,iterations = 1)
        ret,thresh1 = cv2.threshold(erosion,220,255,cv2.THRESH_BINARY)
        cnts, hierarchy = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(cnts) != 0:
            c = max(cnts, key = cv2.contourArea)
            (x,y),radius = cv2.minEnclosingCircle(c)
            center = (int(x),int(y))
            radius = int(radius)
            cv2.circle(self._img,center,radius,(255,0,0),2)

    def start_detection(self):
        if(self.load_image()):
            self.detect_iris()
            #cv2.imshow("IRIS DETECTION", self._img)
            #cv2.waitKey(0)
            self.save_image()
        else:
            print('Image file "' + self._img_path + '" could not be loaded.')


images = []

for file in os.listdir("."):
    if file.endswith(".jpg"):
        path = os.getcwd()
        images.append(os.path.join(path, file))
        
for image in images:
    id = iris_detection(image)
    id.start_detection()
