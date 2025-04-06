# Tracking and Trajectory Extraction

This folder contains scripts to perform object tracking using **YOLOv8 + DeepSORT** and extract trajectory data of specific object classes (e.g., pedestrians) from video footage.

## Contents

| File | Description |
|------|-------------|
| `track_and_save_video.py` | Tracks all objects detected by YOLOv8 and saves a video with bounding boxes and IDs. |
| `track_and_extract_csv.py` | Tracks objects of a specific class (e.g., class ID 11 for pedestrian) and exports per-frame trajectory data as a CSV. |
| `sample_trajectory.csv` | A sample cropped output file showing pedestrian trajectories across 3 video frames. |
| `deepsort/` | DeepSORT module (refer to official repo or install separately). |

---

## Requirements

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- DeepSORT implementation (e.g., from [`mikel-brostrom/Yolov5_DeepSort_Pytorch`](https://github.com/mikel-brostrom/Yolov5_DeepSort_Pytorch))
- `opencv-python`
- `pandas`
- `torch`

Install dependencies:

```bash
pip install ultralytics opencv-python pandas torch

## Script: `track_and_save_video.py`

Tracks all detected objects and saves the output video with bounding boxes and ID labels.

### Usage

```bash
python track_and_save_video.py \
  --video path/to/input_video.mp4 \
  --model path/to/best.pt \
  --output path/to/output_video.mp4

## Script: `track_and_extract_csv.py`

Tracks only objects of a specific class (e.g., pedestrians) and logs their positions frame-by-frame to a CSV file.

### Usage

```bash
python track_and_extract_csv.py \
  --video path/to/input_video.mp4 \
  --model path/to/best.pt \
  --class-id 11 \
  --output trajectory_output.csv

