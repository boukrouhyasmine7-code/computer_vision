from ultralytics import YOLO
import os

# Use the folder of the script's path as working directory 
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Load the YOLO model
model = YOLO("yolov8n.pt")

# Get all .jpg and .png images in the folder
images = [f for f in os.listdir(script_dir) if f.lower().endswith(('.jpg', '.png'))]

# Run detection on each image
for img_file in images:
    print(f"Processing {img_file}...")
    results = model(img_file)  # returns a list
    for r in results:
        r.show()   # display image with detections
        r.save()   # save output to ./runs/detect/
