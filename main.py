from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time


class ObjectDetection:

    def __init__(self, lower=np.array([100, 0, 0]), upper=np.array([120, 255, 100]), x=0, y=0, dimx=640, dimy=400, RED=np.array([0, 0, 255])):
        self.lower = lower
        self.upper = upper
        self.x = x
        self.y = y
        self.RED = RED
        self.dimx = dimx
        self.dimy = dimy

    def gatherPoint(self, frame):
        mask = cv2.inRange(hsv, self.lower, self.upper)

        active = []
        for row in range(0, self.dimx, 10):
            for col in range(0, self.dimy, 10):
                if(mask[col, row] == 255):
                    active.append([row, col])
        return mask, active

    def findobje(self, activelist):

        ave = averageofactive(activelist)
        self.x = ave[0]
        self.y = ave[1]
        obj = [self.x, self.y]
        return obj

    def averageofactive(activelist):
        totalx = 0
        totaly = 0
        count = 0

        for item in activelist:
            totalx = totalx + item[0]
            totaly = totaly + item[1]
            count = count + 1

        if count > 0:
            return [int(totalx / count), int(totaly / count)]
        else:
            return [0, 0]

    def draw(self, obj, frame):

        if obj[0] != 0 or obj[1] != 0:
            cv2.circle(frame, (obj[0], obj[1]), 10, self.RED, 2)


''' main loop starts here '''
dimx = 640

dimy = 400
video = cv2.VideoCapture(0)
p = ObjectDetection()
while(True):
    ret, Frame = video.read()

    frame = cv2.resize(Frame, (dimx, dimy))
    blurred = cv2.GaussianBlur(Frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    mask, Point = p.gatherPoint(hsv)

    cv2.imshow('frame', mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
