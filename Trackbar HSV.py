import cv2
import numpy as np

# Load image
img = cv2.imread("RealXD.png")

def on_trackbar(val):
    # Get current trackbar positions
    h_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
    s_min = cv2.getTrackbarPos("Sat Min", "Trackbars")
    v_min = cv2.getTrackbarPos("Val Min", "Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
    s_max = cv2.getTrackbarPos("Sat Max", "Trackbars")
    v_max = cv2.getTrackbarPos("Val Max", "Trackbars")
    scale_factor = cv2.getTrackbarPos("Scale", "Trackbars") / 100.0

    # Define lower and upper HSV thresholds
    lower_val = np.array([h_min, s_min, v_min])
    upper_val = np.array([h_max, s_max, v_max])

    # Resize image
    scaled_img = cv2.resize(img, None, fx=scale_factor, fy=scale_factor)

    # Convert to HSV
    hsv = cv2.cvtColor(scaled_img, cv2.COLOR_BGR2HSV)

    # Threshold the HSV image
    mask = cv2.inRange(hsv, lower_val, upper_val)

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw merged bounding boxes on original image
    img_with_boxes = scaled_img.copy()  # Make a copy of the scaled image
    for contour in contours:
        # Get bounding box for each contour
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img_with_boxes, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display image with merged bounding boxes
    cv2.imshow("Image with Merged Bounding Boxes", img_with_boxes)


if img is not None:
    # Create a window named 'Trackbars' to adjust HSV thresholds
    cv2.namedWindow("Trackbars")
    cv2.createTrackbar("Hue Min", "Trackbars", 0, 179, on_trackbar)
    cv2.createTrackbar("Sat Min", "Trackbars", 0, 255, on_trackbar)
    cv2.createTrackbar("Val Min", "Trackbars", 0, 255, on_trackbar)
    cv2.createTrackbar("Hue Max", "Trackbars", 179, 179, on_trackbar)
    cv2.createTrackbar("Sat Max", "Trackbars", 255, 255, on_trackbar)
    cv2.createTrackbar("Val Max", "Trackbars", 255, 255, on_trackbar)
    cv2.createTrackbar("Scale", "Trackbars", 100, 200, on_trackbar)

    # Call on_trackbar function to initialize detection with default values
    on_trackbar(0)

    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):  # Press 'q' to quit
            break

    cv2.destroyAllWindows()
else:
    print("Image not found.")

