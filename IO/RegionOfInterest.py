"""
 ROI(Region Of Interest) : 관심영역
 필요한 부분의 영역만 선택하여, 잘라낸 후 연산 처리
 Numpy의 slicing을 활용하여 ROI 선택

 일반적인 이미지의 경우 width , height 순으로 접근하지만,
 ndarray의 경우 행과 열로 구성되어 있기 때문에 height, width 순으로 접근해야 한다
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("../image/img_3.png")

x = 240; y=250; w=50; h=50;
roi = img[y:y+h, x:x+w]

print(roi.shape) # (30, 50, 3)
cv2.rectangle(roi, (0,0), (h-1,w-1),(255,255,255),2)		# ROI 초록색 사각형으로 표시
# rectangle(img, start, end, color)
img2 = roi.copy()		# roi 배열 복사
img[y+h:y+h+h, x:x+w] = roi		# 새로운 좌표에 roi추가, 눈 1개 추가
cv2.rectangle(img, (x,y),(x+w, y+h+h),(255,255,255))

img3 = roi.copy()		# roi 배열 복사
img[y+h+h:y+h+h+h, x:x+w] = roi		# 새로운 좌표에 roi추가, 눈 1개 추가
cv2.rectangle(img, (x,y+h),(x+w, y+h+h+h),(255,255,255))


cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()




