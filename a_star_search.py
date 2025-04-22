import heapq

import pandas as pd


# The function initializes and returns open
def init_open():
    return []


# The function inserts s into open
def insert_to_open(open_list, s):  # Should be implemented according to the open list data structure
    heapq.heappush(open_list, s)


# The function returns the best node in open (according to the search algorithm)
def get_best(open_list):
    return heapq.heappop(open_list)


# The function returns the neighboring locations of s_location
def get_neighbors(grid, s_location):
    rows, cols = grid.shape[0], grid.shape[1]
    row, col = s_location
    neighbors = []
    directions = [
        (-1, 0),  # up
        (0, 1),  # right
        (1, 0),  # down
        (0, -1),  # left
    ]
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols:
            cell = str(grid[new_row, new_col])
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
    return abs(s_location[0] - goal_location[0]) + abs(s_location[1] - goal_location[1])


# Locations are tuples of (x, y)
def astar_search(grid, start_location, goal_location):
    # State = (f, g, h, x, y, s_prev) # f = g + h (For Priority Queue)
    # Start_state = (0, 0, 0, x_0, y_0, False)
    start = (0, 0, 0, start_location[0], start_location[1], False)
    open_list = init_open()
    closed_list = set()
    # Mark the source node as
    # visited and enqueue it
    insert_to_open(open_list, start)
    while not is_empty(open_list):
        # Dequeue a vertex from
        # queue and print it
        s = get_best(open_list)
        # print(s)
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
            h = calculate_heuristic(n_location, goal_location)
            g = s[2] + 1
            f = g + h
            n = (f, h, g, n_location[0], n_location[1], s)
            insert_to_open(open_list, n)
        closed_list.add(s_location)


def print_route(s):
    for r in s:
        print(r)


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
        grid[location] = 'x'
    print(pd.DataFrame(grid))
