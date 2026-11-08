# 🐍 Snake Game

> *"A modern remake of the timeless classic, built with Python and Pygame."*

**Repository:** [github.com/ariya-rajaeinezhad/Snake](https://github.com/ariya-rajaeinezhad/Snake)  
**Role:** Game Developer · **Duration:** 2 Weeks · **Year:** 2025 · **Status:** Completed

---

## 📖 About This Project

This repository contains the complete source code for a modern remake of the classic Snake game, developed in **Python** using the **Pygame** library.

The game features smooth and responsive controls, real-time score tracking, and precise collision detection. Building this project deepened my understanding of game loops, event handling, and object-oriented programming in Python, while also teaching me how to manage state and timing inside a real-time application.

---

## ✨ Key Highlights

- 🎮 **Smooth & Responsive Controls** — Optimized event-queue processing so input is handled exactly once per frame, eliminating input latency.
- 🏆 **Real-Time Score Tracking** — Live score updates that reflect player performance instantly during gameplay.
- 💥 **Robust Collision Detection** — Accurate and reliable logic for both boundary walls and self-collision.
- 🎨 **Polished Arcade Experience** — Dedicated start screen and game-over screen for a complete, satisfying user journey.
- 🏗️ **Object-Oriented Design** — Clean, modular architecture separating game logic, rendering, and state management.

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| **Language** | Python 3.x |
| **Game Library** | Pygame |
| **Architecture** | Object-Oriented Programming (OOP) |
| **Core Concepts** | Game Loop, Event Handling, Collision Detection |

---

## 🎮 How to Play

1. **Start** — Launch the game and begin from the start screen.
2. **Move** — Use the **Arrow Keys** to navigate the snake around the board.
3. **Goal** — Eat the food to grow longer and increase your score.
4. **Avoid** — Do not crash into the walls or your own tail, or it's game over!
5. **Restart** — Try again from the game-over screen and beat your high score.

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed on your machine:
- [Python](https://www.python.org/) (v3.8 or higher recommended)
- [pip](https://pip.pypa.io/en/stable/) (Python package installer)

---

## 🚀 Installation & Setup

### 1. Clone the Repository
`git clone https://github.com/ariya-rajaeinezhad/Snake.git`  
`cd Snake`

### 2. Create a Virtual Environment (Recommended)
`python -m venv venv`

Activate it:
- **Windows:** `venv\Scripts\activate`
- **macOS / Linux:** `source venv/bin/activate`

### 3. Install Dependencies
`pip install pygame`

### 4. Run the Game
`python main.py`

*(Replace `main.py` with the actual entry-point file name if it differs.)*

---

## 🧠 The Challenge

The snake kept responding **one frame late** to key presses, which made the controls feel sluggish and unresponsive.

I dug into how Pygame's **event queue** works and discovered the issue was in how input was being polled inside the loop. By restructuring the loop to process input **exactly once per frame**, the controls became instant and frame-perfect. This taught me how critical timing and event ordering are in real-time applications.

---

## 💡 What I Learned

- **Real-Time Game Loops** — How to maintain a consistent frame rate and separate update logic from render logic.
- **Object-Oriented Programming in Python** — Encapsulating game entities into reusable, self-contained classes.
- **Event-Driven Programming** — Efficiently handling user input via Pygame's event queue without blocking the main thread.
- **State & Timing Management** — Keeping game state predictable across frames and transitions.

---

## 📄 License

Copyright (c) 2025 **Ariya Rajaei Nezhad**. All rights reserved.  
No part of this project may be copied, reproduced, or distributed without permission from the author.

---

## 📬 Let's Connect

- **Email:** [aryarajaeinezhad@gmail.com](mailto:aryarajaeinezhad@gmail.com)
- **LinkedIn:** [linkedin.com/in/ariya-rajaei-nezhad](https://www.linkedin.com/in/ariya-rajaei-nezhad-7a5b9142b/)
- **GitHub:** [github.com/ariya-rajaeinezhad](https://github.com/ariya-rajaeinezhad)
- **Portfolio:** [portfolio-nine-drab-65.vercel.app](https://portfolio-nine-drab-65.vercel.app/)

---

<div align="center">
  <sub>Built with passion, coded with purpose by <strong>Ariya Rajaei Nezhad</strong></sub>
</div>
