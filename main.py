from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time


class ObjectDetection:

    def GetVideo():
        video = cv2.VideoCapture(0)
        return video

    def display(video):
        greyLower = np.array([0, 0, 171])
        greyUpper = np.array([255, 255, 255])
        pts = deque(maxlen=128)

        while(True):
            ret, Frame = video.read()

            frame = imutils.resize(Frame, width=600)
            blurred = cv2.GaussianBlur(Frame, (11, 11), 0)
            hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

            mask = cv2.inRange(hsv, greyLower, greyUpper)
            mask = cv2.erode(mask, None, iterations=2)
            mask = cv2.dilate(mask, None, iterations=2)

            cv2.imshow('frame', mask)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        video.release()
        cv2.destroyAllWindows()

    if __name__ == '__main__':
        vid = GetVideo()
        display(vid)
