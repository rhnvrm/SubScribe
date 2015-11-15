import cv2





#ms = int(raw_input("What is the millisecond of the value you want to save?"))
ms = 5000
videofile = 'test.mp4'

videocapture = cv2.VideoCapture(videofile)
videocapture.set(cv2.cv.CV_CAP_PROP_POS_MSEC,ms)
success, image = videocapture.read()
if success:
    cv2.imwrite('frame%d.jpg' % (ms), image)
    #cv2.imshow('frame%d % (ms)', image)
    #cv2.waitKey()
