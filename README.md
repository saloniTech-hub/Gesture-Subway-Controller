# 🎮 Gesture Subway Controller

### Real-Time Hand Gesture-Based Game Controller Using Computer Vision

A Python-based computer vision project that allows users to control Subway Surfers using hand gestures captured through a webcam. The system uses MediaPipe for hand landmark detection, OpenCV for real-time video processing, and keyboard automation to translate recognized gestures into game actions.

## ✨ Key Features

- Real-time hand detection and tracking
- Finger counting and gesture recognition
- Touch-free Subway Surfers gameplay
- Webcam-based control without physical keyboard interaction
- Integration with the BlueStacks Android emulator
- Modular Python implementation

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core application development |
| OpenCV | Webcam access and image processing |
| MediaPipe | Hand landmark detection |
| PyDirectInput | Keyboard input automation |
| BlueStacks | Running Subway Surfers on Windows |

## ✋ Gesture Controls

| Hand Gesture | Game Action |
|---|---|
| ✊ Closed Fist | Roll / Down |
| ☝️ Index Finger | Move Left |
| ✌️ Two Fingers | Move Right |
| 🖐️ Open Palm | Jump / Up |

## ⚙️ How It Works

1. The webcam captures live video frames.
2. OpenCV processes the captured frames.
3. MediaPipe detects the hand and identifies 21 hand landmarks.
4. Finger-counting logic recognizes the hand gesture.
5. The recognized gesture is mapped to a keyboard action.
6. Subway Surfers responds to the corresponding command through BlueStacks.

## 🧠 Model and Dataset

**Model:** MediaPipe Hands (pre-trained hand detection and landmark models).

**Dataset:** No custom training dataset was used. Hand gestures are identified using rule-based finger counting and real-time webcam input.

## 🚀 Installation and Usage

**1. Clone the repository**

```bash
git clone https://github.com/saloniTech-hub/Gesture-Subway-Controller.git
```

**2. Navigate to the project directory**

```bash
cd Gesture-Subway-Controller
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Start the gesture controller**

```bash
python backend/gesture_controller.py
```

**5.** Open Subway Surfers in BlueStacks and configure the arrow-key controls.

*Note: Add `requirements.txt` before using the installation command above.*

## 📸 Screenshots and Demo

Screenshots and a demonstration video will be added to showcase hand tracking, gesture recognition, and gameplay.

## 🔮 Future Enhancements

- Gesture sensitivity configuration
- Improved gesture stabilization
- Customizable game controls
- Interactive controller dashboard
- Support for additional games

## 👩‍💻 Project Highlights

This project demonstrates practical applications of computer vision, real-time image processing, hand landmark detection, and Python automation in gesture-based human-computer interaction.
