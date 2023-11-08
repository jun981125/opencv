import numpy as np
import matplotlib.pyplot as plt
import cv2

img1 = cv2.imread("../image/img_1.png")
img2 = cv2.imread("../image/img_2.png")
img3 = cv2.imread("../image/img_3.png")


plt.subplot(1,3,1)
plt.imshow(img1[:,:,(2,1,0)])
plt.subplot(1,3,2)
plt.imshow(img2[:,:,::-1])
plt.subplot(1,3,3)
plt.imshow(img3[:,:,(2,1,0)])

plt.show()
