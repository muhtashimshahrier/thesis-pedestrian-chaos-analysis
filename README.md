# thesis-pedestrian-chaos-analysis

This repository contains the full implementation and materials from my undergraduate thesis:

> **Application of Chaos Theory to Evaluate Pedestrian Behavior Using Deep Learning Based Video Analytics in Different Diurnal Variations**  
> Department of Civil Engineering, BUET | March 2025

---

## Overview

In high-density, mixed-traffic cities like Dhaka, pedestrian behavior is complex and often unpredictable — especially under varying light conditions. This thesis explores whether **chaotic patterns** exist in pedestrian movement and whether these patterns vary **between daytime and nighttime**.

To investigate this, I used a combination of:

- **Computer vision** to detect and track pedestrians in urban footage
- **Chaos theory metrics** to quantify behavioral irregularities

The full pipeline involved object detection, trajectory extraction, and quantitative chaos analysis using real-world surveillance video.

---

## Methodology

1. **Dataset Preparation**
   - Raw nighttime video footage was preprocessed using OpenCV
   - Frames were extracted at regular intervals and annotated

2. **Object Detection**
   - A **custom YOLOv8** model was trained to detect 16 road user classes, including pedestrians and vehicles
   - Special focus was placed on performance in low-light environments

3. **Object Tracking & Trajectory Extraction**
   - **DeepSORT** was used to track pedestrian positions across frames
   - Frame-wise coordinates were exported to build trajectory datasets

4. **Chaos Analysis**
   - Two core metrics were used to quantify behavioral unpredictability:
     - **Lyapunov Exponents (LE)** — measures trajectory divergence over time
     - **Approximate Entropy (ApEn)** — quantifies movement irregularity
   - Analysis was performed separately for **daytime** and **nighttime** scenarios

---

## Tools & Libraries

- **Python 3.10+**
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- [DeepSORT](https://github.com/nwojke/deep_sort)
- **OpenCV** – video frame extraction
- **NumPy / pandas** – numerical ops and data formatting
- **matplotlib** – trajectory visualization
- Custom implementations of:
  - Lyapunov Exponent (Rosenstein method)
  - Approximate Entropy

---

## Repository Structure

| Folder | Purpose |
|--------|---------|
| `yolov8_training/` | Training a YOLOv8 model for nighttime road user detection |
| `image_extraction/` | Frame extraction from videos using OpenCV |
| `bbox_conversion/` | Conversion of polygon annotations to YOLO-format bounding boxes |
| `tracking_and_trajectories/` | Object tracking with YOLOv8 + DeepSORT and trajectory data export |
| `chaos_analysis/` | Scripts for computing Lyapunov Exponents and Approximate Entropy |
| `sample_data/` | A sample image and label file for demonstration |
| `thesis_presentation_slide/` | Final presentation slide PDF |

Each folder includes a `README.md` with detailed descriptions and usage guidance.

---

## License

- All **code** in this repository is licensed under the [MIT License](LICENSE).
- The **thesis write-up** and **presentation slides** are licensed under the [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).

---

## Citation

If you find this work helpful in your own research or study, please cite it using:

```bibtex
@thesis{shahrier2025chaos,
  author    = {Md. Muhtashim Shahrier},
  title     = {Application of Chaos Theory to Evaluate Pedestrian Behavior Using Deep Learning Based Video Analytics in Different Diurnal Variations},
  school    = {Bangladesh University of Engineering and Technology (BUET)},
  year      = {2025},
  type      = {Undergraduate Thesis},
  url       = {https://github.com/muhtashimshahrier/thesis-pedestrian-chaos-analysis}
}
```
## About Me

**Md. Muhtashim Shahrier**  
BUET Civil Engineering '25  
[Website](https://muhtashimshahrier.github.io) · [GitHub](https://github.com/muhtashimshahrier)
