import heapq
import math 
import random 
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore
import numpy as np


grid_size = 200
block_size = 1 # Size of each wall block

class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h

    def f(self):
        return self.g + self.h

def astar(start_state, goal_state, heuristic, successors):
    open_set = []
    closed_set = set()


    start_node = Node(start_state)
    heapq.heappush(open_set, (start_node.f(), id(start_node), start_node))

    while open_set:
        _, _, current_node = heapq.heappop(open_set)

        if current_node.state == goal_state:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
                plot(path)
            return path[::-1]

        closed_set.add(current_node.state)
        plot(closed_set)
        watch = successors(current_node.state)

        for successor_state, cost in successors(current_node.state):
            if successor_state in closed_set:
                continue

            g = current_node.g + cost
            h = heuristic(successor_state, goal_state)
            successor_node = Node(successor_state, current_node, g, h)
            heapq.heappush(open_set, (successor_node.f(), id(successor_node), successor_node))

    return None

def heuristic(state, goal_state):
    # Manhattan distance heuristic, better for non diagonal movements
    return abs(state[0] - goal_state[0]) + abs(state[1] - goal_state[1])

    # Euclidean distance heuristic
    # x1, y1 = state
    # x2, y2 = goal_state
    # return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def successors(state):
    x, y = state
    # Possible movements
    moves = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    for dx, dy in moves:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < grid_size and 0 <= new_y < grid_size:
            if (new_x, new_y) not in walls:
                cost = 1 if dx == 0 or dy == 0 else math.sqrt(2)  # Cost is sqrt(2) for diagonal moves
                yield (new_x, new_y), cost


start_state = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
goal_state = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))

while start_state == goal_state:
    start_state = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
    goal_state = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))

walls = set()
for i in range(0, grid_size, block_size):
    for j in range(0, grid_size, block_size):
        if random.random() < 0.3:
            start_x = random.randint(i, min(i + block_size - 1, grid_size - 1))
            start_y = random.randint(j, min(j + block_size - 1, grid_size - 1))
            if (start_x, start_y) != start_state and (start_x, start_y) != goal_state:
                for x in range(start_x, min(start_x + block_size, grid_size)):
                    for y in range(start_y, min(start_y + block_size, grid_size)):
                        walls.add((x, y))

win = pg.GraphicsLayoutWidget(show=True)
win.setWindowTitle('Pathfinding Visualization')
view = win.addViewBox()

img = pg.ImageItem(border='w')
view.addItem(img)

view.setRange(QtCore.QRectF(0, 0, grid_size, grid_size))
win.showFullScreen()

def plot(path):
    global frame_count
    grid = np.zeros((grid_size, grid_size))

    for wall in walls:
        grid[wall] = 1

    if path is not None:
        for node in path:
            grid[node] = 2

    grid[start_state] = 4
    grid[goal_state] = 5

    img.setImage(grid)

    QtCore.QCoreApplication.processEvents() 

path = astar(start_state, goal_state, heuristic, successors)

QtCore.QCoreApplication.instance().exec()
