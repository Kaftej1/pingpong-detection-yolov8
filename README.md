# YOLOv8 Ping-Pong Detection 🏓

## 🔍 Problem Statement

Table tennis refereeing is often subjective and prone to human error. Our project proposes an **AI-powered referee assistant** that:

* Detects and tracks the ping-pong ball in real time.
* Ensures fair play by analyzing ball–table and ball–net interactions.
* Makes refereeing easier and more accurate for tournaments and home games.

---

## 📊 Dataset

* Collected and annotated **table tennis images/videos** (ball, players, interactions).
* Processed with **Roboflow** for training/validation/test splits.
* Data structured as YOLOv8-compatible (`data.yaml`, `train/`, `valid/`, `test/`).

---

## 🧠 Approaches

We explored multiple methods:

1. **Computer Vision–based**: classical ball tracking, segmentation, motion analysis.
2. **Machine Learning–based**: CNNs for feature extraction + reinforcement learning for trajectory prediction & point calculation.
3. **Simulation-based**: physics-informed models of table tennis gameplay.

Final implementation uses **YOLOv8 object detection** fine-tuned on our dataset.

---

## 🚀 Training

* Framework: [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
* Hardware: CPU/GPU (PyTorch backend)
* Epochs: \~50
* Metrics (at 12 epochs):

  * **Precision:** 0.88
  * **Recall:** 0.59
  * **mAP\@50:** 0.65
  * **mAP\@50-95:** 0.49

---


## 🎥 Demo Video

[▶️ Watch the Demo Video](videos/PingPong_Presentation.mp4)


---

## 📦 Installation

```bash
# Clone repo
git clone https://github.com/Kaftej1/pingpong-detection-yolov8.git
cd pingpong-detection-yolov8

# Install requirements
pip install -r requirements.txt

# Run detection on images
yolo task=detect mode=predict model=runs/detect/train2/weights/best.pt source=table-tennis-11/test/images show=True save=True conf=0.3

# Run detection on video
yolo task=detect mode=predict model=runs/detect/train2/weights/best.pt source=videos/pingpong.mp4 show=True save=True conf=0.3
```

---

## 📈 Business Model

* **Revenue**: premium subscriptions (\$2–15), donations.
* **Costs**: hosting (\$3/month), R\&D, dataset labeling.
* **Target Users**:

  * Professional & casual players.
  * Referees & tournament organizers.
  * Content creators.
  * Table tennis federations.

---

## ✅ Future Work

* Improve ball tracking in **fast-motion scenarios**.
* Add **point calculation logic** (net hits, table bounces).
* Extend system to **other sports** (tennis, badminton).
