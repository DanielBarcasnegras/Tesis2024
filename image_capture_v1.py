#!/usr/bin/env python3

import cv2
import depthai as dai
import os
from datetime import datetime
import time

# Create pipeline
pipeline = dai.Pipeline()

camRgb = pipeline.create(dai.node.ColorCamera)
camRgb.setBoardSocket(dai.CameraBoardSocket.CAM_A)
camRgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_12_MP)

xoutRgb = pipeline.create(dai.node.XLinkOut)
xoutRgb.setStreamName("rgb")
camRgb.video.link(xoutRgb.input)

# Connect to device and start pipeline
with dai.Device(pipeline) as device:

    # Output queue will be used to get the rgb frames from the output defined above
    qRgb = device.getOutputQueue(name="rgb", maxSize=30, blocking=False)

    # Create directory to save images
    dirName = "/home/drbarcasnegras/Desktop/rgb_data"
    os.makedirs(dirName, exist_ok=True)

    # Add a small delay to allow the camera to stabilize
    time.sleep(60)

    # Capture a single picture
    inRgb = qRgb.get()  # Blocking call, waits until a new data arrives
    frame = inRgb.getCvFrame()
    fName = f"{dirName}/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
    cv2.imwrite(fName, frame)
    print(f"Captured single image: {fName}")

cv2.destroyAllWindows()  # Close OpenCV windows
