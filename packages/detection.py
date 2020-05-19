from packages import *


class ObjectDetection:
    '''
        A class that is used to detect the object location in the frame and mark it through opencv cv2.circle method.


            '''

    def __init__(self, lower=np.array([100, 0, 0]), upper=np.array([120, 255, 100]), x=0, y=0, dimx=640, dimy=400, RED=(0, 0, 255)):
        ''' To initialize all the  variables that are used in the functions below,
            So that I can access each variable in function through self.variablename method. '''

        self.lower = lower  # lower = The lower boundary of selected color
        self.upper = upper  # upper = The upper boundary of selected color
        self.x = x  # x, y = They are the location of object in the given frame
        self.y = y
        self.RED = RED  # RED = the value of red color
        self.dimx = dimx  # dimx, dimy = these are the size of the frame that is captured from cam
        self.dimy = dimy

    def gatherPoint(self, frame):
        ''' To gather the active points when frame is masked
            frame is passed on in a loop after converting it to hsv to mask the frame and get the highlighted object in the frame'''
        mask = cv2.inRange(frame, self.lower, self.upper)  # To mask the frame so that object can be highlighted in black and white contrast

        active = []  # array to store all the active (highlighted points in the frame)
        for row in range(0, self.dimx, 10):  # To loop throgh all rows and columns in the frame. (as assigned the size is 640*400)
            for col in range(0, self.dimy, 10):
                if(mask[col, row] == 255):  # condition to check if the current location in the loop is white?
                    active.append([row, col])  # if its white then store that point in the array using append method
        return mask, active  # whenever this function is called it gives 2 outputs they are masked frame and active points

    def findobje(self, activelist):
        '''     After generating active points from gatherPoint function uing findobje function to find the center. 
                x,y is used to localize the object where active points are merged in center. '''

        totalx = 0
        totaly = 0
        count = 0

        for item in activelist:  # To iterate through all elemets in the array active form gatherPoint function
            totalx = totalx + item[0]  # count all x's
            totaly = totaly + item[1]  # count all y's
            count = count + 1  # a reading for total number of times the loop is iterated
        if totalx != 0:
            self.x = int(totalx / count)  # average point of x's
            self.y = int(totaly / count)  # average point of y's
            obj = [self.x, self.y]
            return obj, self.x, self.y  # whenever this function is called it gives 3 outputs they are x, y which is the location of object in the frame and its combination.
        else:
            print("Object is not located")

    def drawcircle(self, objectloc, frame):
        '''     after the x,y is found, draw the circle using opencv function which takes parameter as objecloc 
                which is an array of both [x,y] '''

        if objectloc[0] != 0 or objectloc[1] != 0:  # The function only runs when the condition where x, y are not 0 i.e. only when an object is detected
            cv2.circle(frame, (objectloc[0], objectloc[1]), 10, self.RED, 2)  # Function to draw the circle at x, y using opencv

    # def drawGraph(self, x, y):
        # pass
    # To convert the Matplotlib figure to a PIL Image and return it
    '''def fig2img(self, fig):

        buf = io.BytesIO()
        fig.savefig(buf)
        buf.seek(0)
        img = Image.open(buf)
        return img '''

    def Display(self, name, frame):
        cv2.imshow(name, frame)
