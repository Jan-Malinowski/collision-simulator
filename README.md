# ⚙️ 1D & 2D Collision Simulation

**Language:** Python  
**Library:** Pygame  

---

## 📖 Overview
This project simulates **elastic collisions** between two objects of different masses.  
- **Current version:** 1D collisions between two squares moving along a single axis.  
- **In progress:** 2D collisions between circles with velocity components in both **X** and **Y** directions.

---

## 🧠 Physics Principles
- **Conservation of Momentum**  
  The total momentum before and after the collision remains constant.

- **Conservation of Kinetic Energy** *(elastic collisions)*  
  The total kinetic energy is preserved during the collision.

- **Collision Detection**  
  - **1D:** Triggered when the edges of the squares meet.  
  - **2D (planned):** Triggered when the distance between two circle centers is less than or equal to the sum of their radii.

- **Velocity Update Formulas**  
  - **1D:** Uses standard elastic collision equations for two masses along a line.  
  - **2D (planned):** Uses vector-based formulas to separate velocity into **normal** and **tangent** components, updating only the normal component after collision.

---

## ✨ Features
- Real-time simulation with Pygame’s rendering loop.
- Adjustable **masses** and **initial velocities**.
- Smooth, visually clear animation of motion and collisions.

---

## 🚀 Planned Improvements
- Implementation of 2D elastic collisions for circles.
- Optional inelastic collision mode with adjustable restitution coefficient.
- Additional visual effects and statistics display.

---
## 📺 Previev
<img width="889" height="620" alt="prev" src="https://github.com/Jan-Malinowski/collision-simulator/blob/main/preview.gif" />

<img width="889" height="620" alt="prev" src="https://github.com/user-attachments/assets/939808e0-ec1c-4e8c-980c-91012ee16a53" />


