# Pathfinding Visualizer

This Python script visualizes the A* pathfinding algorithm on a grid. It uses the PyQtGraph library to display the grid and the progress of the algorithm.

## Dependencies

- Python 3
- PyQtGraph
- NumPy
- heapq

## How it works

The script defines a `Node` class to represent each node in the pathfinding algorithm. Each `Node` has a `state`, a `parent`, and `g` and `h` values which represent the cost to reach the node and the heuristic cost to the goal respectively.

The `astar` function implements the A* pathfinding algorithm. It takes a `start_state`, a `goal_state`, a `heuristic` function, and a `successors` function as arguments. The `heuristic` function calculates the heuristic cost from a state to the goal, and the `successors` function generates the successors of a state.

The `astar` function uses a priority queue to keep track of the nodes to be explored (the open set), and a set to keep track of the nodes that have been explored (the closed set). It starts by adding the `start_state` to the open set, and then enters a loop where it pops the node with the lowest `f` value from the open set, adds it to the closed set, and explores its successors. The loop continues until the open set is empty or the `goal_state` is found.

## Usage

To run the script, simply execute it with Python:

```bash
python pathfinding.py
```
The script will display a window with a grid. The start state, goal state, and walls are randomly generated. The A* algorithm will start running immediately, and the progress of the algorithm will be visualized on the grid.

Customization
You can customize the size of the grid and the size of the wall blocks by modifying the `grid_size` and `block_size` variables at the top of the script.
