import cv2
import numpy as np

def ColorDetection(frame):
    
    # Converting to HSV Color frame
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Blue Color 63, 72, 49
    low_blue = np.array([50, 50, 49])
    high_blue = np.array([255, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask = blue_mask)
    blue_mask = cv2.medianBlur(blue_mask, 5)

    # Getting the contours
    contours,_ = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnts in contours:
        area = cv2.contourArea(cnts)
        if area > 1:
            return True

    return False