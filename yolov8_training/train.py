# yolov8_training/train.py

"""
YOLOv8 Training Script for Road User's Detection

This script trains a YOLOv8l model using a custom dataset configured in okiish.yaml.
"""

from ultralytics import YOLO

def main():
    model = YOLO("yolov8l.pt")  # You can change to yolov8s.pt or other variants
    model.train(
        data="okiish.yaml",     # Dataset configuration file
        epochs=1500,
        imgsz=640,
        batch=8,
        workers=8,
        device=0,               # Change to 'cpu' if no GPU is available
        save_period=10,
        patience=1000
    )

if __name__ == "__main__":
    main()
