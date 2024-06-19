import cv2

# Load the original high-resolution image
img = cv2.imread("RealXD.png")
if img is None:
    print("Image not found.")
    exit()

# Define the scale factor for displaying the image
scale_factor = 0.35  # Adjust this scale factor as needed

# Calculate the new dimensions
scaled_width = int(img.shape[1] * scale_factor)
scaled_height = int(img.shape[0] * scale_factor)

# Resize the image for display
scaled_img = cv2.resize(img, (scaled_width, scaled_height))

# Define a uniform size for all bounding boxes (original and scaled)
box_width_original = 475
box_height_original = 650

# Calculate scaled dimensions
box_width_scaled = int(box_width_original * scale_factor)
box_height_scaled = int(box_height_original * scale_factor)

# Define the number of bounding boxes and their positions
num_boxes = 8  # Example: 5 bounding boxes
start_x_original = 60  # Starting x-coordinate for the first bounding box (original)
start_y_original = 40  # Starting y-coordinate for the first bounding box (original)
spacing_original = 0  # Spacing between bounding boxes (original)

# List to store the generated ROIs
generated_rois = []

# Calculate and store bounding boxes in both original and scaled dimensions
for i in range(num_boxes):
    # Calculate original coordinates
    x_original = start_x_original + i * (box_width_original + spacing_original)
    y_original = start_y_original
    roi_original = (x_original, y_original, box_width_original, box_height_original)
    
    # Calculate scaled coordinates
    x_scaled = int(x_original * scale_factor)
    y_scaled = int(y_original * scale_factor)
    roi_scaled = (x_scaled, y_scaled, box_width_scaled, box_height_scaled)
    cv2.rectangle(scaled_img, (x_scaled, y_scaled), (x_scaled + box_width_scaled, y_scaled + box_height_scaled), (0, 255, 0), 2)
    
    # Append both original and scaled ROIs to the list
    generated_rois.append((roi_original, roi_scaled))

# Print the generated ROIs (original and scaled)
print("Generated ROIs:")
for idx, (roi_original, roi_scaled) in enumerate(generated_rois):
    print(f"ROI {idx + 1}:")
    print(f"  Original - x={roi_original[0]}, y={roi_original[1]}, width={roi_original[2]}, height={roi_original[3]}")
    print(f"  Scaled   - x={roi_scaled[0]}, y={roi_scaled[1]}, width={roi_scaled[2]}, height={roi_scaled[3]}")

cv2.imshow("Image with Bounding Boxes", scaled_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


