import numpy as np
import cv2

# openCV 에서 이미지를 출력하기 위해서 ndarray의 타입은 uint8
img = np.zeros((120,120), dtype=np.uint8)
img2 = np.zeros((120,120,3), dtype=np.uint8)

# 2차원 이미지
img[25:35, :] = 45
img[55:65, :] = 115
img[85:95, :] = 160
img[:,35:45] = 205
img[:,75:85] = 255

# 3차원 이미지
img2[25:35, :] = [255,0,0]
img2[55:65, :] = [0,255,0]
img2[85:95, :] = [0,0,255]
img2[:,35:45] = [255,255,0]
img2[:,75:85] = [255,0,255]


cv2.imshow('gray', img)
cv2.imshow('color', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()