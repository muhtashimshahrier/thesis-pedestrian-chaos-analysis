# Polygon to Bounding Box Converter

This script converts polygon-based label annotations into standard bounding box format (YOLOv8-compatible). It was used to preprocess detection labels for my undergraduate thesis on pedestrian behavior analysis.

---

## What It Does

- Detects whether annotations are in polygon format (more than 2 points)
- Converts them to `(x_center, y_center, width, height)` format
- Skips any entries where the image is not found

---

### Command-Line Example

```bash
python polygon_to_bbox.py \
  --input_dir ../data/labels_raw/ \
  --output_dir ../data/labels_bbox/ \
  --image_dir ../data/images/
```
## Notes
- Assumes .txt and .jpg filenames match (e.g., 12.txt ↔ 12.jpg)
- Format matches YOLO: class_id x_center y_center width height
