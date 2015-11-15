import cv2
import pysrt

def mid(x,y):
	return (x+y)/2

def save_new_frame(file, ms, text):

	videocapture = cv2.VideoCapture(videofile)
	videocapture.set(cv2.cv.CV_CAP_PROP_POS_MSEC,ms)
	success, image = videocapture.read()
	
	height, width = image.shape[:2]

	if success:
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(image,text,(10,height-10), font, 0.4,(255,255,255),1)
		cv2.imwrite('frame%03d.jpg' % (ms/1000), image)
		#cv2.imshow('frame%d % (ms)', image)
	    #cv2.waitKey()	

if __name__ == "__main__":

	subs = pysrt.open('comedian/test.srt')
	videofile = 'comedian/test.mp4'

	for i in xrange(0, len(subs)):
		ms = mid(subs[i].start.seconds*1000,subs[i].end.seconds*1000)
		save_new_frame(videofile, ms, str(subs[i].text))
