import cv2
import numpy as np
import os
import mysql.connector
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from mysql.connector import Error

class ImageHandler(FileSystemEventHandler):
    def __init__(self, folder_path, db_config):
        self.folder_path = folder_path
        self.lower_val = np.array([25, 40, 40])
        self.upper_val = np.array([100, 255, 255])
        self.rois = [
            (60, 40, 475, 650, "Label 1"),
            (535, 40, 475, 650, "Label 2"),
            (1010, 40, 475, 650, "Label 3"),
            (1485, 40, 475, 650, "Label 4"),
            (1960, 40, 475, 650, "Label 5"),
            (2435, 40, 475, 650, "Label 6"),
            (2910, 40, 475, 650, "Label 7"),
            (3385, 40, 475, 650, "Label 8")
        ]
        self.db_config = db_config

    def on_created(self, event):
        if event.src_path.endswith(".png"):
            print(f"New image detected: {event.src_path}")
            self.process_image(event.src_path)

    def process_image(self, filepath):
        max_attempts = 15
        attempt = 0
        delay = 3  # Increase delay to 3 seconds

        while attempt < max_attempts:
            try:
                if os.path.exists(filepath):
                    img = self.load_image(filepath)
                    print(f"Image loaded: {filepath}")
                    hsv_img = self.convert_to_hsv(img)
                    mask = self.create_green_mask(hsv_img)
                    green_pixel_counts = self.process_rois(img, mask)
                    self.upload_to_database(filepath, img, green_pixel_counts)
                    print(f"Processing complete: {filepath}")
                    break  # Exit loop if processing is successful
                else:
                    raise FileNotFoundError(f"File does not exist: {filepath}")
            except FileNotFoundError as e:
                print(e)
                print(f"Attempt {attempt + 1}/{max_attempts} failed. Retrying in {delay} seconds...")
                attempt += 1
                time.sleep(delay)
            except Error as e:
                print(f"Error: {e}")
                # Retry mechanism
                print("Retrying in 5 seconds...")
                time.sleep(5)  # Wait for 5 seconds before retrying

    def load_image(self, filepath):
        img = cv2.imread(filepath)
        if img is None:
            raise FileNotFoundError(f"Image not found at path: {filepath}")
        return img

    def convert_to_hsv(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    def create_green_mask(self, hsv_image):
        return cv2.inRange(hsv_image, self.lower_val, self.upper_val)

    def process_rois(self, image, mask):
        green_pixel_counts = {}
        for i, (x, y, w, h, label) in enumerate(self.rois):
            roi_mask = mask[y:y+h, x:x+w]
            green_pixel_count = cv2.countNonZero(roi_mask)
            green_pixel_counts[label] = green_pixel_count

            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            print(f"{label}: {green_pixel_count} green pixels")
        
        return green_pixel_counts

    def upload_to_database(self, filepath, img, green_pixel_counts):
        # Read the image as binary data
        with open(filepath, 'rb') as file:
            binary_data = file.read()

        connection = mysql.connector.connect(**self.db_config)
        cursor = connection.cursor()

        attempt = 0
        max_attempts = 3  # Adjust the number of retry attempts as needed
        retry_delay = 5  # Adjust the delay between retries as needed

        while attempt < max_attempts:
            try:
                # Insert image data and green pixel counts into the database
                cursor.execute("""
                    INSERT INTO images (image_name, image_data, label1_count, label2_count, label3_count, label4_count, label5_count, label6_count, label7_count, label8_count)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    os.path.basename(filepath),
                    binary_data,
                    green_pixel_counts.get("Label 1", 0),
                    green_pixel_counts.get("Label 2", 0),
                    green_pixel_counts.get("Label 3", 0),
                    green_pixel_counts.get("Label 4", 0),
                    green_pixel_counts.get("Label 5", 0),
                    green_pixel_counts.get("Label 6", 0),
                    green_pixel_counts.get("Label 7", 0),
                    green_pixel_counts.get("Label 8", 0)
                ))
                connection.commit()
                print(f"Data uploaded to database for {os.path.basename(filepath)}")
                break  # Exit loop if successful
            except mysql.connector.Error as e:
                print(f"Error while inserting into MySQL: {e}")
                if attempt < max_attempts - 1:
                    print(f"Retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)
                else:
                    print(f"Max retry attempts ({max_attempts}) exceeded. Exiting.")
                    raise e  # Raising the error to handle it outside this method
            finally:
                attempt += 1

        cursor.close()
        connection.close()

def main():
    folder_path = "E:/rgb-data"
    db_config = {
        'host': '127.0.0.1',
        'user': 'root',
        'database': 'image_data'
    }

    event_handler = ImageHandler(folder_path, db_config)
    observer = Observer()
    observer.schedule(event_handler, path=folder_path, recursive=False)
    observer.start()

    print("Monitoring started. Press Ctrl+C to stop.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Monitoring stopped.")
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
