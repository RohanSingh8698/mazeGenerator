import numpy as np
import random

def generate_maze(width, height):
    maze = np.ones((height, width))  # Start with all walls
    # List to store the frontier cells
    frontier = []
    # Start from a cell
    start_x, start_y = 1, 1
    maze[start_x][start_y] = 0
    # Add neighboring walls of the starting cell to the frontier
    frontier.extend([(start_x+2, start_y, start_x+1, start_y), 
                     (start_x-2, start_y, start_x-1, start_y),
                     (start_x, start_y+2, start_x, start_y+1),
                     (start_x, start_y-2, start_x, start_y-1)])
    
    while frontier:
        # Select a random wall
        fx, fy, px, py = random.choice(frontier)
        frontier.remove((fx, fy, px, py))
        
        # If the cell beyond the wall is not carved:
        if fx >= 0 and fy >= 0 and fx < width and fy < height and maze[fx][fy] == 1:
            # Make the wall a passage
            maze[px][py] = 0
            maze[fx][fy] = 0
            # Add the neighboring walls of the cell to the frontier
            if fx + 2 < width:
                frontier.append((fx+2, fy, fx+1, fy))
            if fx - 2 >= 0:
                frontier.append((fx-2, fy, fx-1, fy))
            if fy + 2 < height:
                frontier.append((fx, fy+2, fx, fy+1))
            if fy - 2 >= 0:
                frontier.append((fx, fy-2, fx, fy-1))
    
    return maze

# Generate a 100x100 maze
large_maze = generate_maze(100, 100)

# Optional: Save the maze to a file for later visualization or usage
# np.savetxt("large_maze.csv", large_maze, delimiter=",", fmt="%d")

print("Maze generated successfully.")
