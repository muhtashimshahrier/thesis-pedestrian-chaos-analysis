# YOLOv8 Training – Pedestrian Detection

This folder contains the code and related files used to train a custom YOLOv8 object detection model as part of my undergraduate thesis. The model was trained to detect 16 different pedestrian and vehicle classes from day and night surveillance video footage.

---

## 🧠 Overview

- **Base model:** YOLOv8l (`yolov8l.pt`)
- **Classes:** 16 total (e.g., Pedestrian, Rickshaw, Truck, etc.)
- **Training epochs:** 1500
- **Image size:** 640x640
- **Batch size:** 8
- **Framework:** [Ultralytics YOLOv8](https://docs.ultralytics.com)

---

## 📁 Files

| File                        | Description                                  |
|----------------------------|----------------------------------------------|
| `train.py`                 | Main training script using YOLOv8 API        |
| `okiish.yaml`              | Dataset configuration (paths + class names) |
| `yolov8_training_metrics.png` | Training/validation losses, mAP, precision/recall curves |
| `confusion_matrix.png`     | Final confusion matrix on validation data    |

---

## 🧾 Dataset Structure (referenced in `okiish.yaml`)

dataset/
├── images/
│   ├── train/
│   ├── val/
│   └── test/
├── labels/
│   ├── train/
│   ├── val/
│   └── test/


Each image has a corresponding YOLO-format label file in the `labels/` directory.

---

## 🛠️ Command Summary

```bash
# Train the model (runs from train.py)
python train.py
