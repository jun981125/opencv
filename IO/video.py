import cv2

video_file = "../image/big_buck.avi"

cap = cv2.VideoCapture(video_file)	# 비디오 캡쳐 객체 cap 생성
if cap.isOpened():					# 지정된 파일이 정상적으로 초기화 된다면, isOpened() 는 True를 반환
	while True:
		ret, img = cap.read()		# 다음 프레임 읽기
		if ret:
			cv2.imshow(video_file, img)
			cv2.waitKey(25)			# 각 프레임을 화면에 표시하는 시간 25ms : 40fps
			# 계산방법 : 지연시간 = 1000 % fps
		else:
			print('재생 완료')
			break
else:
	print('객체 초기화 실패')
cap.release()						# 캡처 객체 초기화 실패
cv2.destroyAllWindows()
