# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 03:16:49 2019

@author: Baazigar
"""

import cv2
import numpy as np
import imutils

def main():
    path = "C:\\Users\\Baazigar\\Desktop\\Images for project\\"
    imgpath1 =  path + "Side_4.png"
    imgpath2 =  path + "Side_4+9.png"
    print (imgpath2)
    img1 = cv2.imread(imgpath1, 1)
    img2 = cv2.imread(imgpath2, 1)
    img1 = cv2.resize(img1,(512,512))
    img2 = cv2.resize(img2,(512,512))

    cv2.imshow("cars",img2)
    cv2.waitKey(0)
    
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    cv2.imshow("ref",img1)
    cv2.waitKey(0)
    cv2.imshow("cars",img2)
    cv2.waitKey(0)

    img1 = cv2.GaussianBlur(img1,(7,7),0) #removes gaussian noise
    img2 = cv2.GaussianBlur(img2,(7,7),0)
    cv2.imshow("ref",img1)
    cv2.waitKey(0)
    cv2.imshow("cars",img2)
    cv2.waitKey(0)
    
    img1 = cv2.medianBlur(img1,3) 
    img2 = cv2.medianBlur(img2,3)#removes salt and pepper noise
    cv2.imshow("ref",img1)
    cv2.waitKey(0)
    cv2.imshow("cars",img2)
    cv2.waitKey(0)
    
    img1 = cv2.Canny(img1,30,150,L2gradient = True) #canny edge detection
    img2 = cv2.Canny(img2,30,150,L2gradient = True)
    
    cv2.imshow("ref",img1)
    cv2.waitKey(0)
    cv2.imshow("cars",img2)
    cv2.waitKey(0)
    #trying dialation
    
    kernel = np.ones((3,3),np.uint8)
    img1 = cv2.dilate(img1,kernel,iterations = 3)
    cv2.imshow("ref",img1)
    cv2.waitKey(0)
    img2 = cv2.dilate(img2,kernel,iterations = 3)
    cv2.imshow("cars",img2)
    cv2.waitKey(0)
    
    res = cv2.absdiff(img1, img2)
    cv2.imshow("rem",res)
    cv2.waitKey(0)
#--- convert the result to integer type ---
    res = res.astype(np.uint8)

#--- find percentage difference based on number of pixels that are not zero ---
    percentage = (np.count_nonzero(res) * 100)/ res.size
    print (int(percentage*(10/8.304977416992188))+11) 
    
'''

    cnts_1 = cv2.findContours(img1.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts_1 = imutils.grab_contours(cnts_1)
    output_1 = img1.copy()
    for c in cnts_1:
        cv2.drawContours(output_1,[c],-1,(120,120,120),5)
        cv2.imshow("vs",output_1)
        cv2.waitKey(0)
    print (len(cnts_1))
    
    cnts_2 = cv2.findContours(img2.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts_2 = imutils.grab_contours(cnts_2)
    cnts_2 = sorted(cnts_2, key=cv2.contourArea, reverse=True)[:9]
    
    output_2 = img2.copy()
    for c in cnts_2:
        cv2.drawContours(output_2,[c],-1,(120,120,120),5)
        cv2.imshow("vs",output_2)
        cv2.waitKey(0)
    
    print (len(cnts_2))

'''
if __name__ == "__main__":
    main()
