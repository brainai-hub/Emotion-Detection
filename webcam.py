import av
import cv2
import numpy as np
import streamlit as st
from streamlit_webrtc import WebRtcMode, webrtc_streamer

def video_frame_callback(frame: av.VideoFrame) -> av.VideoFrame:
    print("here")
    image = frame.to_ndarray(format="bgr24")
    print(np.shape(image))

    cv2.rectangle(image, (0, 0), (10, 20), (0,0,0), 2)

    return av.VideoFrame.from_ndarray(image, format="bgr24")




webrtc_ctx = webrtc_streamer(
    key="object-detection",
    mode=WebRtcMode.SENDRECV,
 
    video_frame_callback=video_frame_callback,
    media_stream_constraints={"video": True, "audio": False},
    async_processing=True,
)