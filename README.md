# OpenGL Maze Generator & Solver

This project is a Python-based application that generates and solves a maze visually using OpenGL and PyOpenGL.

# How It Works

1. Maze Generation
The maze is generated using the Depth-First Search (DFS) algorithm.

- The algorithm visits random neighboring cells
- Walls are removed to create paths
- A stack is used for backtracking when dead ends are reached

This ensures all cells in the maze are connected.

# 2. Maze Solver
After generation, the maze is solved automatically using wall-following and backtracking logic.

# Visualization
- Green Dot → Current mouse position
- Red Path → Explored route
- Blue Dots → Dead ends
  
The solver continues until it reaches the maze exit.

# Data Structures

The maze uses two 2D arrays:

- `northWall[R][C]` → Horizontal walls
- `eastWall[R][C]` → Vertical walls

Values:
- `1` → Wall exists
- `0` → Wall removed

# Features
- Dynamic maze generation
- DFS-based maze generation
- Automatic maze solving
- Real-time OpenGL visualization
- Path rendering
- Dead-end highlighting
- Random cycle creation

# Requirements

Install dependencies:

```bash
pip install PyOpenGL PyOpenGL_accelerate
```

Run the Program

```bash
python Running-Maze.py
```
The maze will generate and solve automatically.
