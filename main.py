
from packages import *

from packages import detection


if __name__ == '__main__':

    ''' main loop starts here '''
    dimx = 640
    dimy = 400
    video = cv2.VideoCapture(0)  # To start webcam
    p = detection.ObjectDetection()  # creating a object of class ObjectDetection in detection.py
    #x, y = [], []
    while(True):  # A loop which reads all captured frames making it a video
        ret, Frame = video.read()  # Reading the frames and storing it as Frame and also a bolean to store True if Frame is stored and False if not

        frame = cv2.resize(Frame, (dimx, dimy))  # To resize the size of frame
        blurred = cv2.GaussianBlur(Frame, (11, 11), 0)  # To blur the frame to remove noise
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)  # To convert frame from BGR to HSV so that we can deted the color that is given in HSV color code

        mask, Points = p.gatherPoint(hsv)  # gatherPont function in detection.py

        objectloc, pointx, pointy = p.findobje(Points)  # findobje function in detection.py

        p.drawcircle(objectloc, frame)  # drawcircle function in detection.py
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
        GRID_SIZE = 20  # To make a grid on frame

        height, width, channels = frame.shape  # To store the shape of frame i.e 640 400 3
        for x in range(0, width - 1, GRID_SIZE):  # To create vertical lines based on the size of the frame
            cv2.line(frame, (x, 0), (x, height), (255, 0, 0), 1, 1)
        for x in range(0, height - 1, GRID_SIZE):  # To create Horrizontal lines based on the size of the frame
            cv2.line(frame, (0, x), (width, x), (255, 0, 255), 1, 1)

        print(frame.shape)
        p.Display('object_blue', mask) # To display mask frame using cv2.imshow method
        p.Display('detection', frame) # To display grid frame using cv2.imshow method anddisplay function.

        if cv2.waitKey(1) & 0xFF == ord('q'): # Stop the loop if q is pressed on keyboard
            break

    video.release() # Stop reading frames
    cv2.destroyAllWindows() # close all windows that are running because of imshow method.
