import cv2
import numpy as np


"""
    read picture
"""
img = cv2.imread('images/....jpg')

img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2)) # (width, height)

# grap image img[0:100, 0:150] #width, height
img = cv2.GaussianBlur(img, (9, 9), 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img = cv2.Canny(img, 200, 200)

kernel = np.ones((5, 5), np.uint8)
img = cv2.dilate(img, kernel, iteration = 1)

img = cv2.erode(img, kernel, iteration = 1)

cv2.imshow('Result', img) # width, height

cv2.waitKey(0)



"""
    read mp4 video
"""
cap = cv2.VideoCapture('videos/....mp4')

while True:
    success, img = cap.read()
    cv2.imshow('Result', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



"""
    read web camera
"""
cap = cv2.VideoCapture(0)
cap.set(3, 500) #width indicator = 3
cap.set(4, 300) #height indicator = 4

while True:
    success, img = cap.read()
    cv2.imshow('Result', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break