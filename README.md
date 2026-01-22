# AI-Powered Basketball Match Analysis System  
## Robotics Club Summer Project

Automated Basketball Intelligence using Computer Vision and Machine Learning

---

## Introduction

The **AI Basketball Match Analysis System** is an end-to-end computer vision and machine learning project developed as part of the **Robotics Club Summer Project**.

The system extracts meaningful tactical and performance insights from standard basketball match videos. By combining object detection, tracking, perspective transformation, and real-world metric computation, it converts raw footage into structured analytics useful for players, coaches, and analysts.

---

## The Problem

Traditional basketball analytics systems rely on:

- Manual data annotation  
- Expensive motion tracking hardware  
- Proprietary software  

This makes advanced analysis inaccessible to:

- Amateur teams  
- College-level players  
- Students and independent analysts  

---

## Our Solution

We built an **AI-driven basketball analysis pipeline** that processes standard broadcast basketball videos and automatically extracts structured insights.

The system can:

- Detect players and the basketball  
- Track player and ball movement across frames  
- Assign players to teams  
- Identify ball possession, passes, and interceptions  
- Calculate real-world player speed and distance  
- Generate a tactical top-down court view  

---

## Key Features

### Object Detection and Tracking
- YOLO-based detection of players, ball, and referees
- Multi-object tracking across frames

### Automatic Team Assignment
- Zero-shot image classification
- Jersey-color based team identification

### Ball Possession Analysis
- Tracks possession changes
- Detects passes and interceptions

### Tactical Top-Down View
- Perspective transformation (homography)
- Bird’s-eye court visualization

### Speed and Distance Estimation
- Real-world metric computation using court dimensions

---

## Technology Stack

- **Python**
- **Ultralytics YOLO (YOLOv5 / YOLOv8)**
- **OpenCV**
- **NumPy**
- **Roboflow**
- **Hugging Face Zero-Shot Classifier**

---
## Project Structure

basketball_analysis/
├── input_videos/        # Input basketball match videos
├── models/              # Trained YOLO models
├── training_notebooks/  # Model training notebooks
├── main.py              # Main execution script
└── README.md

## Contributors

Robotics Club Summer Project

Akhil Prakash
Anshika Sharma
Pragya Agarwal

## Future Scope

- Shot detection and success prediction
- Player heatmaps and movement visualization
- Advanced tactical and play-type analysis
- Web-based interactive analytics dashboard
  
## Installation

```bash
git clone https://github.com/your-username/basketball_analysis.git
cd basketball_analysis
pip install ultralytics roboflow
