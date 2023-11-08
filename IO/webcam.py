import cv2

cap = cv2.VideoCapture(0)						# os에 따라 다름
												# 현재 0 : 아이폰  1 : MAC cam
x=100; y=100;
if cap.isOpened():
	while True:
		ret, img = cap.read()
		if ret:
			cv2.imshow('camera', img)
			"""
			cv2.moveWindow("title",x,y)
			key = cv2.waitKey(0) & 0xFF
			print(key, chr(key))
			if key == ord('w'):
				y +=10
			elif key == ord('s'):
				y-=10
			elif key == ord('a'):
				x -=10
			elif key == ord('d'):
				x +=10
			elif key == ord('q') or key ==27:
				break
				cv2.destroyAllWindows()
			cv2.moveWindow('title', x, y)"""
			if cv2.waitKey(1) != -1:			# 1ms동안 키 입력 대기
				break							# 종료
		else:
			print('no frame')
			break
else:
	print('웹캠을 연결할 수 없음')
cap.release()
cv2.destroyAllWindows()
