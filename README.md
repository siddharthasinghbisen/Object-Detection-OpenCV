# Object-detection-OpenCV
To detect an on object and to plot the x and y (on the point at which cv2 circle is drawn).
Working of project is shown in the gif below:

![](detection.gif)

The poject is based on detecting an object of certain  HSV color range using webcam. Following are the steps involved in detection:

-> The project follows around opencv library.

-> Using opencv frames are gathered through webcam and stored in a variable.

-> Stored Frames are looped through.

-> All the frames are then blurred to remove noise and converted from BGR to HSV as the color range of object that is to be detected
   is givven in betten two range of HSV color code.

-> A function is made that takes frames, Masks them and tries to find out all the highligted points(active points in the frame).
   Masking is a proces where given image in converted in black and white contrast where white is the part that  is in the range of given HSV color code. The function returns all active points.

-> Findobje functions is created which takes all active points and tries to find the center part in the highlighted region by taking
   average of all active points. Another way to do this could be through using opencv findContours method. This function returns x,y coordinates of object in the frame.
   
-> Using drawcircle function a circle is created at the x,y position to show that object is found!

