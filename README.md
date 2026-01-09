# 🎯 Aim Trainer – Python & Pygame

A fast-paced **aim training game** built using **Python** and **Pygame**. This project simulates a reflex-based targeting exercise where players click on dynamically spawning targets while tracking speed, accuracy, and reaction performance.

The project focuses on **real-time input handling**, **timed events**, and **game-loop optimization**, making it ideal for learning and showcasing interactive game mechanics.

---

## 📌 Project Overview
The Aim Trainer challenges players to click on expanding and shrinking targets before they disappear. The game tracks detailed performance metrics such as:
- Time elapsed
- Hits and misses
- Click accuracy
- Target hit speed (targets per second)

The game ends when the player runs out of lives due to missed targets.

---

## 🎮 Gameplay Mechanics
- Targets spawn at fixed time intervals
- Each target grows to a maximum size and then shrinks
- Clicking inside a target counts as a hit
- Missed or expired targets reduce lives
- Game ends when lives reach zero

---

## 📁 File Structure
```text
Aim_Trainer/
│
├── aim-trainer.py      # Main game file
```

---

## 🛠️ Core Concepts Used
- Game loop and frame control
- Timed events using `pygame.USEREVENT`
- Mouse input detection
- Collision detection using Euclidean distance
- Dynamic UI rendering (stats bar & end screen)
- Basic performance analytics

---

## 🧠 Code Architecture

### `Target` Class
Responsible for:
- Managing target size animation
- Drawing layered circles for visual feedback
- Detecting mouse collision

### Game Loop (`main()`)
- Handles events and input
- Updates target states
- Tracks gameplay statistics
- Renders UI and end screen

---

## 🖥️ User Interface

### Top Stats Bar
Displays real-time information:
- Time elapsed
- Hit speed (targets per second)
- Total hits
- Remaining lives

### End Screen
Summarizes performance:
- Total time
- Hit speed
- Accuracy percentage

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Pygame

Install dependencies:
```bash
pip install pygame
```

---

## ▶️ Running the Game
```bash
python aim-trainer.py
```

---

## 🎯 Controls
| Action | Input |
|---|---|
| Shoot target | Left Mouse Button |
| Exit game | Close Window |

---

## 📈 Skills Demonstrated
- Python programming
- Pygame-based game development
- Real-time input processing
- Event-driven architecture
- Game statistics and analytics

---

## 🧪 Learning Outcomes
- Understanding timing-based mechanics
- Designing responsive game feedback loops
- Managing game state and end conditions
- Improving accuracy and reflex-based logic

---

## 🏷️ Portfolio Note
This project demonstrates **interactive systems design** and **real-time user input handling**, making it a strong addition to:
- Game development portfolios
- Python learning projects
- Interactive application showcases

---

## 🔮 Possible Improvements
- Difficulty scaling over time
- Sound effects and visual feedback
- Leaderboard or score saving
- Pause / restart functionality
- Converting this into a 3D movement based aim trainer, simulating real FPS games

---

**Author:** Spondan Bandyopadhyay

---
