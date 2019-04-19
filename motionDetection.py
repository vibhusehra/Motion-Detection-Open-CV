import cv2
import sys
import numpy as np
'''How does this work? We take 2 consecutive frames, if there is a minor change
nothing is detected, but if there is a big change, motion is detected'''

#start capturing
cam = cv2.VideoCapture(0)

#read the last 2 frames
ret,lastFrame = cam.read()
ret,currentFrame = cam.read()

#convert current to grayscale
gray = cv2.cvtColor(currentFrame,cv2.COLOR_BGR2GRAY)

i=0
while True:
	lastFrame = currentFrame
	ret,currentFrame = cam.read()
	gray = cv2.cvtColor(currentFrame,cv2.COLOR_BGR2GRAY)

	#finding absolute diff. by the last frame and current frame
	diff = cv2.absdiff(lastFrame,currentFrame)

	# i += 1
	# if i%10 == 0:
	# 	i = 0
	# 	print("current: ",np.mean(currentFrame))
	# 	print("diff: ", np.mean(diff))
	if np.mean(diff) > 10:
		print("Motion Detected!!")

	cv2.imshow('Video',diff)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		
cam.release()
cv2.destroyAllWindows()
