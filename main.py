from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import pandas as pd
import time
import matplotlib.pyplot as plt

from itertools import count
import matplotlib.animation as animation
class ObjectDetection:

    def __init__(self, lower=np.array([100, 0, 0]), upper=np.array([120, 255, 100]), x=0, y=0, dimx=640, dimy=400, RED=(0, 0, 255)):
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

        totalx = 0
        totaly = 0
        count = 0

        for item in activelist:
            totalx = totalx + item[0]
            totaly = totaly + item[1]
            count = count + 1

        self.x = int(totalx / count)
        self.y = int(totaly / count)
        obj = [self.x, self.y]
        return obj, self.x, self.y

    def drawcircle(self, objectloc, frame):

        if objectloc[0] != 0 or objectloc[1] != 0:
            cv2.circle(frame, (objectloc[0], objectloc[1]), 10, self.RED, 2)

    def drawGraph(self, x, y):
        plt.cla()
        plt.plot(x, y, label='x and y coordinates for obj')

        plt.legend(loc='upper left')
        plt.tight_layout()


if __name__ == '__main__':

    ''' main loop starts here '''
    dimx = 640
    dimy = 400
    video = cv2.VideoCapture(0)
    p = ObjectDetection()
    x, y = [], []
    while(True):
        ret, Frame = video.read()

        frame = cv2.resize(Frame, (dimx, dimy))
        blurred = cv2.GaussianBlur(Frame, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        mask, Points = p.gatherPoint(hsv)
        objectloc, pointx, pointy = p.findobje(Points)
        p.drawcircle(objectloc, frame)
        cv2.imshow('frame', frame)

        x.append(pointx)
        y.append(pointy)

        ani = animation.FuncAnimation(plt.gcf(), p.drawGraph(x, y), interval=1000)
        plt.tight_layout()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    plt.show()
    video.release()
    cv2.destroyAllWindows()
