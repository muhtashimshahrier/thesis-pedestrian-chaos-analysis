# Sample Data

This folder contains a single example image and its corresponding YOLO-format label file, provided for demonstration purposes.

---

## Contents

| File          | Description                            |
|---------------|----------------------------------------|
| `example.jpg` | A sample frame extracted from video    |
| `example.txt` | YOLOv8-format label file for the image |

---

## Label Format

The label file follows the standard **YOLOv8 annotation format**:
<class_id> <x_center> <y_center> <width> <height>


All coordinates are normalized to the range `[0, 1]` relative to image width and height.

---

## Notes

- This is only a **sample pair** for illustrative purposes.
- Full training and validation data were not uploaded due to size and privacy considerations.

