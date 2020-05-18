from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import pandas as pd
import time
import matplotlib.pyplot as plt
import io
from PIL import Image

from itertools import count
import matplotlib.animation as animation


class ObjectDetection:
    '''
            lower = The lower boundary of selected color
            upper = The upper boundary of selected color
            x, y = They are the location of object in the given frame
            dimx, dimy = these are the size of the frame that is captured from cam
            RED = the value of red color'''

    def __init__(self, lower=np.array([100, 0, 0]), upper=np.array([120, 255, 100]), x=0, y=0, dimx=640, dimy=400, RED=(0, 0, 255)):
        self.lower = lower
        self.upper = upper
        self.x = x
        self.y = y
        self.RED = RED
        self.dimx = dimx
        self.dimy = dimy
    # To gather the active points when frame is masked

    def gatherPoint(self, frame):
        mask = cv2.inRange(hsv, self.lower, self.upper)

        active = []
        for row in range(0, self.dimx, 10):
            for col in range(0, self.dimy, 10):
                if(mask[col, row] == 255):
                    active.append([row, col])
        return mask, active
    # After generating active points from gatherPoint function uing findobje function to find the center. x,y is used to localize the object where active points are merged in center
    def findobje(self, activelist):

        totalx = 0
        totaly = 0
        count = 0

        for item in activelist:
            totalx = totalx + item[0]
            totaly = totaly + item[1]
            count = count + 1
        if totalx != 0:
            self.x = int(totalx / count)
            self.y = int(totaly / count)
            obj = [self.x, self.y]
            return obj, self.x, self.y
        else:
            print("Object is not located")
    # after the x,y is found, draw the circle using opencv function which takes parameter as objecloc which is an array of both [x,y]
    def drawcircle(self, objectloc, frame):

        if objectloc[0] != 0 or objectloc[1] != 0:
            cv2.circle(frame, (objectloc[0], objectloc[1]), 10, self.RED, 2)

    # def drawGraph(self, x, y):
        # pass
    # To convert the Matplotlib figure to a PIL Image and return it
    '''def fig2img(self, fig):

        buf = io.BytesIO()
        fig.savefig(buf)
        buf.seek(0)
        img = Image.open(buf)
        return img '''


if __name__ == '__main__':

    ''' main loop starts here '''
    dimx = 640
    dimy = 400
    video = cv2.VideoCapture(0)
    p = ObjectDetection()
    #x, y = [], []
    while(True):
        ret, Frame = video.read()

        frame = cv2.resize(Frame, (dimx, dimy))
        blurred = cv2.GaussianBlur(Frame, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        # gatherPont
        mask, Points = p.gatherPoint(hsv)
        # findobje
        objectloc, pointx, pointy = p.findobje(Points)
        # drawcircle
        p.drawcircle(objectloc, frame)
        # To plot x,y in graph for every frame
        # x.append(pointx)
        # y.append(pointy)
        #plt.scatter(x, y, label='x and y coordinates for obj')
        # gcf is to get the current figure
        #fig = plt.gcf()
        # The figure is converted to img
        #img = p.fig2img(fig)
        # img is converted into array for cv2 to load
        #img2 = np.array(img)
        # To display the video detecting the object and also plot x,y respectively
        GRID_SIZE = 20

        height, width, channels = frame.shape
        for x in range(0, width - 1, GRID_SIZE):
            cv2.line(frame, (x, 0), (x, height), (255, 0, 0), 1, 1)
        for x in range(0, height - 1, GRID_SIZE):
            cv2.line(frame, (0, x), (width, x), (255, 0, 255), 1, 1)

        print(frame.shape)
        cv2.imshow('object', mask)
        cv2.imshow('detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()
