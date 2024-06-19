import cv2

# Load the original high-resolution image
img = cv2.imread("RealXD.png")
if img is None:
    print("Image not found.")
    exit()

# Define the scale factor for displaying the image
scale_factor = 0.3  # Adjust this scale factor as needed

# Calculate the new dimensions
scaled_width = int(img.shape[1] * scale_factor)
scaled_height = int(img.shape[0] * scale_factor)

# Resize the image for display
scaled_img = cv2.resize(img, (scaled_width, scaled_height))

rois = []

while True:
    # Select ROI on the scaled-down image
    roi = cv2.selectROI("Select ROI and press SPACE or ENTER (press 'c' to confirm and finish)", scaled_img, showCrosshair=True, fromCenter=False)
    
    # Check if ROI has a valid size
    if roi[2] == 0 or roi[3] == 0:
        break
    
    # Add the selected ROI to the list
    rois.append(roi)
    
    # Draw the selected ROI on the scaled image (for visual feedback)
    cv2.rectangle(scaled_img, (roi[0], roi[1]), (roi[0] + roi[2], roi[1] + roi[3]), (0, 255, 0), 2)
    
    # Show the updated image with drawn ROIs
    cv2.imshow("Select ROI and press SPACE or ENTER (press 'c' to confirm and finish)", scaled_img)
    
    key = cv2.waitKey(0) & 0xFF
    if key == ord('c'):
        break

cv2.destroyAllWindows()

# Print the scaled ROIs
print("Scaled ROIs:", rois)

# Adjust the ROIs to the original image size
original_rois = [
    (
        int(roi[0] / scale_factor),
        int(roi[1] / scale_factor),
        int(roi[2] / scale_factor),
        int(roi[3] / scale_factor)
    )
    for roi in rois
]

# Print the original ROIs
print("Original ROIs:", original_rois)

# Draw all ROIs on the original image
for (x, y, w, h) in original_rois:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the original image with all ROIs
cv2.imshow("Image with ROIs", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
