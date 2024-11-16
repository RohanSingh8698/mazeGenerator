from collections import deque
import time
import numpy as np
import matplotlib.pyplot as plt
from maze import complex_maze

# Define a complex maze
start = (0, 0)  # Start position
end = (60, 49)  # End position

def dfs_maze(maze, start, end):
    """ Perform DFS to find a path from start to end in a maze. """
    stack = [start]
    came_from = {start: None}
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left

    while stack:
        current = stack.pop()
        if current == end:
            break
        for dx, dy in directions:
            nx, ny = current[0] + dx, current[1] + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0 and (nx, ny) not in came_from:
                stack.append((nx, ny))
                came_from[(nx, ny)] = current

    if current == end:  # Reconstruct the path
        path = []
        while current:
            path.append(current)
            current = came_from[current]
        return path[::-1]
    return None

# Time the execution of DFS
start_time = time.time()
path = dfs_maze(complex_maze, start, end)
end_time = time.time()

if path:
    viz_maze = np.array(complex_maze).astype(float)
    for x, y in path:
        viz_maze[x, y] = 0.5  # Path marked with 0.5
    fig, ax = plt.subplots()
    cmap = plt.cm.viridis  # Viridis colormap for better visualization
    ax.imshow(viz_maze, cmap=cmap, interpolation='nearest')
    ax.plot(start[1], start[0], "gs", markersize=10)  # Start marker
    ax.plot(end[1], end[0], "rs", markersize=10)  # End marker
    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()
    print(f"Path found in {end_time - start_time:.4f} seconds.")
else:
    print("No path found in the maze.")
