import cv2
import base64
from PIL import Image
import sys
from resizeimage import resizeimage
vidcap = cv2.VideoCapture('test.mp4')
success,image = vidcap.read()
count = 0;
f=open("text.txt","w")
while success:
	success,image = vidcap.read()
	cv2.imwrite("test1/frame%d.jpg" % count, image)     # save frame as JPEG file
	if cv2.waitKey(10) == 27:                     # exit if Escape is hit
		break
	with open("test1/frame%d.jpg" % count, "rb") as imageFile:
		str = base64.b64encode(imageFile.read())
		f.write(str)
		f.write("\n")
	count += 1
	

print count
f.close()
