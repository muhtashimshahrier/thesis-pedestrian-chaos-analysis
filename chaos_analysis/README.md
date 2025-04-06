# Chaos Analysis of Pedestrian Trajectories

This folder contains scripts and result plots used to analyze the **chaotic nature of pedestrian movements** in different diurnal conditions (e.g., day vs. night). The analysis is based on trajectory data extracted using YOLOv8 + DeepSORT, and is performed using two chaos-theoretic metrics:

- **Lyapunov Exponent (LE)** — Measures trajectory divergence over time
- **Approximate Entropy (ApEn)** — Measures movement regularity or randomness

---

## Folder Structure

| File / Folder | Description |
|---------------|-------------|
| `lyapunov_analysis.py` | Python implementation of Rosenstein’s method to compute Lyapunov Exponents |
| `apen_analysis.py` | Python script for computing Approximate Entropy of velocity and direction change |
| `lyapunov_result_day.png`, `lyapunov_result_night.png` | Histogram plots of Lyapunov Exponents |
| `apen_result_day.png`, `apen_result_night.png` | Histogram plots of Approximate Entropy |
| `README.md` | This file |

---

## What Do These Metrics Tell Us?

| Metric | High Value = | Low Value = |
|--------|---------------|-------------|
| **Lyapunov Exponent** | High sensitivity, chaos, randomness | Predictable or stable trajectories |
| **Approximate Entropy** | Irregular/unpredictable behavior | More structured or repetitive behavior |

You can use these metrics to detect how pedestrians behave differently in **day vs. night** conditions.

---

## 🔁 Workflow Summary

### 1. **Input**  
All scripts take a CSV file of pedestrian trajectories, formatted like:

| Frame | ObjectID | x1 | y1 |
|-------|----------|----|----|

Same format as `sample_trajectory.csv` from the tracking stage.

---

### 2. **Lyapunov Exponent Calculation**  
Run:

```bash
python lyapunov_analysis.py
```
### 3. **Approximate Entropy Calculation**
Run:

```bash
python apen_analysis.py
