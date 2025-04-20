import pandas as pd
import heapq  # For priority queue


# The function initializes and returns open
def init_open():
    return []  # Will be used as a heap (priority queue)


# The function inserts s into open
def insert_to_open(open_list, s):
    heapq.heappush(open_list, s)  # Add to the priority queue


# The function returns the best node in open (according to the search algorithm)
def get_best(open_list):
    if not open_list:
        raise ValueError("open_list is empty, cannot get best node")
    return heapq.heappop(open_list)  # Get the node with the lowest f-value


# The function returns the neighboring locations of s_location
def get_neighbors(grid, s_location):
    """Returns the neighboring locations of s_location in the grid, including diagonals."""
    rows, cols = len(grid), len(grid[0])
    row, col = s_location
    neighbors = []
    # Include all 8 directions: up, right, down, left, and diagonals
    directions = [
        (-1, 0),  # up
        (0, 1),  # right
        (1, 0),  # down
        (0, -1),  # left
        (-1, -1),  # up-left
        (-1, 1),  # up-right
        (1, 1),  # down-right
        (1, -1)  # down-left
    ]
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols:
            cell = str(grid[new_row, new_col])  # Convert to string for NumPy compatibility
            if cell == '.':
                neighbors.append((new_row, new_col))
    return neighbors


# The function returns True if s_location is the goal location and False otherwise
def is_goal(s_location, goal_location):
    return s_location == goal_location


# The function returns True if open_list is empty and False otherwise
def is_empty(open_list):
    return not open_list


# The function estimates the cost to get from s_location to goal_location
def calculate_heuristic(s_location, goal_location):
    """Calculate the Manhattan distance between s_location and goal_location."""
    return abs(s_location[0] - goal_location[0]) + abs(s_location[1] - goal_location[1])


# Locations are tuples of (x, y)
def astar_search(grid, start_location, goal_location):
    # State = (f, h, g, x, y, s_prev) # f = g + h (For Priority Queue)
    # Start_state = (0, 0, 0, x_0, y_0, None)
    h_start = calculate_heuristic(start_location, goal_location)
    start = (h_start, h_start, 0, start_location[0], start_location[1], None)  # f = g + h
    open_list = init_open()
    closed_list = set()
    insert_to_open(open_list, start)
    while not is_empty(open_list):
        s = get_best(open_list)
        s_location = (s[3], s[4])
        if s_location in closed_list:
            continue
        if is_goal(s_location, goal_location):
            print("The number of expansions by AStar Search:", len(closed_list))
            return s
        neighbors_locations = get_neighbors(grid, s_location)
        for n_location in neighbors_locations:
            if n_location in closed_list:
                continue
            g = s[2] + 1  # Increment g by 1 (uniform cost per step)
            h = calculate_heuristic(n_location, goal_location)
            f = g + h
            n = (f, h, g, n_location[0], n_location[1], s)
            insert_to_open(open_list, n)
        closed_list.add(s_location)
    return None  # Goal not found


def print_route(s):
    while s:
        print(s[3], s[4])
        s = s[5]


def get_route(s):
    route = []
    while s:
        s_location = (s[3], s[4])
        route.append(s_location)
        s = s[5]
    route.reverse()
    return route


def print_grid_route(route, grid):
    for location in route:
        row, col = location
        grid[row][col] = 'x'
    print(pd.DataFrame(grid))
