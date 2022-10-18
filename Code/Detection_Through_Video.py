import cv2
import numpy as np
import sys

sys.path.insert(0, './Helper')
from Helper.Motion_Detection import MotionDetection
isclosed = 0

def main():
    while True:

        # Capturing video
        video = cv2.VideoCapture('../pebrin database/7.09.2022.mp4')

        if MotionDetection(video) == False:
            break 

        if isclosed:
            break

    video.release()

    # Destroying all the windows
    cv2.destroyAllWindows()

if __name__== "__main__":
    main()
