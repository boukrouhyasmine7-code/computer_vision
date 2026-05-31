from ultralytics import YOLO
import cv2
import os

# Make Python use the folder of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

video_source = 0  # default webcam Later, you can replace this with a drone camera URL for real flights
cap = cv2.VideoCapture(video_source)

if not cap.isOpened():
    print("Error: Cannot open video source")
    exit()

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS)) if cap.get(cv2.CAP_PROP_FPS) > 0 else 20

# Create a VideoWriter to save the output
out = cv2.VideoWriter(
    "output_detected.avi",
    cv2.VideoWriter_fourcc(*'XVID'),
    fps,
    (frame_width, frame_height)
)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot read frame")
        break

    # Run detection
    results = model(frame)

    # Draw boxes
    frame_with_boxes = results[0].plot()

    # Display
    cv2.imshow("YOLOv8 Live", frame_with_boxes)

    # Save the frame to video
    out.write(frame_with_boxes)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
print("Video saved as output_detected.avi")