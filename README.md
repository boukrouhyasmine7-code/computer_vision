# YOLOv8 Real-Time & Static Object Detection Pipeline

A clean, production-ready Python implementation of an object detection pipeline leveraging the state-of-the-art **YOLOv8 (Nano)** architecture. This project features two distinct processing streams: a high-efficiency batch processing script for static images and a real-time tracking pipeline optimized for webcam or live video feeds.

Developed with modularity in mind, this setup serves as a foundational vision framework suitable for edge-computing deployments, robotics, or autonomous systems (such as UAV navigation feeds).

---

##  Key Features

* **Real-Time Video Stream Processing:** Latency-optimized inference using OpenCV to capture, annotate, and write processed video frames dynamically.
* **Automated Batch Inference:** Dynamic directory scanning that automatically detects, filters, and processes local image batches (`.jpg`, `.png`).
* **Embedded & Edge Optimization:** Core architecture utilizes the `yolov8n.pt` checkpoint (packaged at ~6.2MB), delivering fast inference speeds without sacrificing deployment flexibility.
* **Automated Exporting:** The live video pipeline instantly compiles frames into an engineered `output_detected.avi` asset using the XVID codec.

---

##  Repository Structure

```text
├── computer_vision_4livevideo.py       # Live webcam processing and video generation pipeline
├── computer_vision_4static_images.py      # Automated batch processing script for local images
├── yolov8n.pt                             # Pre-trained YOLOv8 Nano weight checkpoint (COCO)
├── Meredith.jpg and benjamin.jpg  # Batch sample assets for static analysis
└── README.md                              # Project documentation
