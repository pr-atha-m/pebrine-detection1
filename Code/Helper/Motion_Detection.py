from json import detect_encoding
import cv2
import numpy as np
from Helper.Color_Detection import *
global detected



def MotionDetection(video):
    global detected
    
    detected = False

    static_back = None

    # Infinite while loop to treat stack of image as video
    while True:
        
        # Reading frame(image) from video
        check, frame = video.read()

        if check:

            # Converting color image to gray_scale image
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # In first iteration we assign the value
            # of static_back to our first frame
            if static_back is None:
                static_back = gray
                continue

            # Difference between static background
            # and current frame(which is GaussianBlur)
            diff_frame = cv2.absdiff(static_back, gray)

            # If change in between static background and
            # current frame is greater than 30 it will show white color(255)
            thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1]
            thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)

            # Finding contour of moving object
            cnts,_ = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for contour in cnts:
                
                (x, y, w, h) = cv2.boundingRect(contour)

                # Extracting the contour
                extractedContour = frame[y:y+h,x:x+w]

                isValid = ColorDetection(extractedContour)
                if isValid:
                    cv2.rectangle(frame, (x - 1, y - 1), (x + w + 1, y + h + 1), (0, 255, 0), 2)
                    cv2.putText(frame, "Status: {}".format('Detected'), (20, 25), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 0, 255), 2)
                    detected = True

            # Displaying color frame with contour of motion of object
            cv2.imshow("Pebrin Detection [Press E to Exit]", frame)
            

            key = cv2.waitKey(1)
            
            # If q entered whole process will stop
            if key == ord('q'):
                while True:
                    key2 = cv2.waitKey(1)
                    if key2 == ord('q'):
                        break
                    cv2.imshow("Color Frame", frame)
                break

            # Break the process if Key e is pressed
            if key == ord('e'):
                break
        else:
            break
    return detected
