import random
import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# --- CONFIGURATION AND DIMENSIONS ---
R, C = 20, 25
CELL_SIZE = 30
WINDOW_WIDTH = C * CELL_SIZE
WINDOW_HEIGHT = R * CELL_SIZE

# --- DATA STRUCTURE DEFINITIONS ---
# northWall[i][j] tracks horizontal walls; eastWall[i][j] tracks vertical walls
northWall = [[1 for _ in range(C)] for _ in range(R + 1)]
eastWall = [[1 for _ in range(C + 1)] for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]

# --- STATE MANAGEMENT ---
stack = []
current_cell = (0, 0)
visited[0][0] = True
generating = True
solving = False

# --- SOLVER STATE (WALL FOLLOWER) ---
direction = 1  # 0:N, 1:E, 2:S, 3:W
mouse_position = (R - 1, 0)
path = []
dead_ends = set()
visited_solver = set()
ENABLE_CYCLES = True

# --- OPENGL INITIALIZATION ---
def init():
    glClearColor(0, 0, 0, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutCreateWindow(b"Maze Generator + Wall Follower + Cycles")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(20, update, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()
