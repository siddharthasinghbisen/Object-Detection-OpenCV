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

        while(True):
            ret, Frame = video.read()
            cv2.imshow('frame', Frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        video.release()
        cv2.destroyAllWindows()

    if __name__ == '__main__':
        vid = GetVideo()
        display(vid)
