# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 12:46:13 2019

@author: LALIT ARORA
"""

#import numpy 
import cv2
import operator
import numpy as np

class pupil_detection():
    def __init__(self, image_path):
        '''
        initialize the class and set the class attributes
        '''
        self._img = None
        self._img_path = image_path
        self._pupil = None
        self._centroid = None
        
    def load_image(self):
        '''
        load the image based on the path passed to the class
        it should use the method cv2.imread to load the image
        it should also detect if the file exists
        '''
        self._img = cv2.imread(self._img_path)
        # If the image doesn't exists or is not valid then imread returns None
        if type(self._img) == None:
            return False
        else:
            return True
    
    def show_image (self,img):
        cv2.imshow("Result",img)
        cv2.waitKey(0)
    
    def centroid (self):
        # convert image to grayscale image
        gray_image = cv2.cvtColor(self._img, cv2.COLOR_BGR2GRAY)
        # convert the grayscale image to binary image
        ret,thresh = cv2.threshold(gray_image,127,255,0)
        # calculate moments of binary image
        M = cv2.moments(thresh)
        # calculate x,y coordinate of center
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        self._centroid = (cX,cY)
        #cv2.circle(self._img, (cX, cY), 5, (255, 255, 255), -1)
        
    def detect_pupil (self):
        dst = cv2.fastNlMeansDenoisingColored(self._img,None,10,10,7,21)
        blur = cv2.GaussianBlur(dst,(5,5),0)
        inv = cv2.bitwise_not(blur)
        thresh = cv2.cvtColor(inv, cv2.COLOR_BGR2GRAY)
        kernel = np.ones((2,2),np.uint8)
        erosion = cv2.erode(thresh,kernel,iterations = 1)
        ret,thresh1 = cv2.threshold(erosion,210,255,cv2.THRESH_BINARY)
        cnts, hierarchy = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        flag = 10000
        final_cnt = None
        for cnt in cnts:
            (x,y),radius = cv2.minEnclosingCircle(cnt)
            distance = abs(self._centroid[0]-x)+abs(self._centroid[1]-y)
            if distance < flag :
                flag = distance
                final_cnt = cnt
            else:
                continue
        (x,y),radius = cv2.minEnclosingCircle(final_cnt)
        center = (int(x),int(y))
        radius = int(radius)
        cv2.circle(self._img,center,radius,(255,0,0),2)
        
        self._pupil = (center[0],center[1],radius)
        self.show_image(self._img)
        
    def start_detection(self):
        if(self.load_image()):
            self.centroid()
            self.detect_pupil()
        else:
            print('Image file "' + self._img_path + '" could not be loaded.')
        
id = pupil_detection(r'<absolute image path>')
id.start_detection()
