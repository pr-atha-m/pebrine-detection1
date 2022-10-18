import cv2
import numpy as np
import sys
import os
sys.path.insert(0, './Helper')
import streamlit as st
from Helper.Motion_Detection import MotionDetection
st.title("Pebrin Visualisation System")
c1, c2  = st.columns(2)


with c1:
    if st.button("Set Camera"):
        st.text("Press E to Close Camera")
        # define a video capture object

        vid = cv2.VideoCapture(0)
        
        while(True):
            
            # Capture the video frame
            # by frame
            ret, frame = vid.read()
        
            # Display the resulting frame
            cv2.imshow('Set Camera: Press E to exit', frame)
            
            # the 'q' button is set as the
            # quitting button you may use any
            # desired button of your choice
            if cv2.waitKey(1) & 0xFF == ord('e'):
                break
        
        # After the loop release the cap object
        vid.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

with c2:
    if st.button("Start Detection"):

        video = cv2.VideoCapture(0)
        isclosed = 0

        detected = MotionDetection(video)
        video.release()

        # Destroying all the windows
        cv2.destroyAllWindows()

        
        if detected:
            st.subheader("Status ✅ Detected")
        else:
            st.subheader("Status Not ❌ Detected")



hide_streamlit_style = """
            <style>
            footer {visibility: visible;}
            footer:after{
                content:'Copyright @ 2022';
                display:block;
                position:relative;
                color: tomato;
                 

            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
