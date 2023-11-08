import cv2
import matplotlib.pyplot as plt

img_file = "../image/img_3.png"
save_file = "../image_write_test/IMG.png"
img = cv2.imread(img_file, cv2.IMREAD_COLOR)

# IMREAD_COLOR : 기본 값(컬러) 			IMREAD_GRAYSCALE : 그레이 스케일

#plt.imshow(img)
plt.imshow(img[:,:,::-1])
# img[:,:,::] 마지막 축의 길이가 3이므로  img[:,:,:]와 같은 코드
# 마지막 축의 요소를 뒤집기 위해 img[:,:,::-1] 로 처리
# img[:,:,(2,1,0)] 로 표현 할 수 있음

plt.show()
# open CV의 경우 RGB를  B,G,R 순으로 해석하지만,
# matplotlib의 경우엔 R,G,B 순으로 해석하기 때문에 색상의 위치가 뒤바뀜.

if img is not None:
	cv2.imshow('IMG', img)		# 이미지 화면에 표시
	cv2.waitKey(0)						# 키가 입력될 때 까지 대기
	cv2.destroyAllWindows()				# 모든 창 닫기
	cv2.imwrite(save_file,img)			# 저장할 경로 및 이름 / 저장할 포맷

else:
	print('No image file')