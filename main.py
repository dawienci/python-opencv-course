import cv2
import numpy as np

photo = np.zeros((450, 1000, 3), dtype='uint8')

# RGB standart format
# BGR format OpenCV
photo[100:150, 200:250] = 255, 0, 0

cv2.rectangle(photo, (0,0), (100,100), (255,0,0), thickness=cv2.FILLED)

cv2.line(photo, (0,0), (100,0), (255,0,0), thickness=2)

cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 50, (255,0,0), thickness=2)

cv2.putText(photo, 'Text', (100,150), cv2.FONT_HERSHEY_TRIPLEX, 1, (255,0,0), thickness=3)

cv2.imshow('Photo', photo)
cv2.waitKey(0)
