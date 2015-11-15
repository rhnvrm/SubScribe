import cv2
import pysrt

def mid(x,y):
	return (x+y)/2

def save_new_frame(ms, text):
	#ms = int(raw_input("What is the millisecond of the value you want to save?"))
	#ms = 5000
	videofile = 'test.mp4'

	videocapture = cv2.VideoCapture(videofile)
	videocapture.set(cv2.cv.CV_CAP_PROP_POS_MSEC,ms)
	success, image = videocapture.read()
	
	if success:
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(image,'Hello World!',(10,500), font, 1,(255,255,255),2)
		cv2.imwrite('frame%d.jpg' % (ms/1000), image)
		#cv2.imshow('frame%d % (ms)', image)
	    #cv2.waitKey()	

subs = pysrt.open('test.srt')

for i in xrange(0, len(subs)):
	ms = mid(subs[i].start.seconds*1000,subs[i].end.seconds*1000)
	save_new_frame(ms, "hello world")



