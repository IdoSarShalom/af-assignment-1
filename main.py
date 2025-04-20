import a_star_search as astar
import breadth_first_search as bfs
from route_grid import create_grid
import time
import copy

ROUTE_LEN_1 = 39
ROUTE_LEN_2 = 291

def run_bfs(grid, start, end, print_route=False, grid_copy=None):
    """Run BFS algorithm and return route and execution time."""
    start_time = time.time()
    solution = bfs.bfs(grid, start, end)
    route = bfs.get_route(solution)
    exec_time = round(time.time() - start_time, 4)
    if print_route:
        print("BFS route: ")
        bfs.print_grid_route(route, grid_copy)
    return route, exec_time

def run_astar(grid, start, end, print_route=False, grid_copy=None):
    """Run A* algorithm and return route and execution time."""
    start_time = time.time()
    solution = astar.astar_search(grid, start, end)
    route = astar.get_route(solution)
    exec_time = round(time.time() - start_time, 4)
    if print_route:
        print("AStar route: ")
        astar.print_grid_route(route, grid_copy)
    return route, exec_time

def print_algorithm_results(algorithm_name, route_length, exec_time):
    """Print results for an algorithm's run."""
    print(f"--- {algorithm_name} solver ---")
    print(f"Route length: {route_length}")
    print(f"Running time: {exec_time}")

def validate_results(bfs_route, astar_route, astar_time, bfs_time, test_num):
    """Validate the results of both algorithms."""
    if len(bfs_route) != len(astar_route):
        return False
    if test_num == 1:
        return len(bfs_route) == ROUTE_LEN_1
    elif test_num == 2:
        if len(bfs_route) == ROUTE_LEN_2:
            if astar_time < bfs_time:
                return True
            else:
                print("Running time is too high for AStar")
                return False
    return False

def test_grid(test_num=1, print_route=False):
    """Test both algorithms on a grid and return validation result."""
    grid, start, end = create_grid(test_num)
    grid_copy = copy.copy(grid) if print_route else None

    # Run BFS
    bfs_route, bfs_time = run_bfs(grid, start, end, print_route, grid_copy)
    print_algorithm_results("BFS", len(bfs_route), bfs_time)

    # Run A*
    astar_route, astar_time = run_astar(grid, start, end, print_route, grid_copy)
    print_algorithm_results("AStar", len(astar_route), astar_time)

    # Validate results
    return validate_results(bfs_route, astar_route, astar_time, bfs_time, test_num)

def run_tests():
    """Run tests for both problem instances."""
    print("------------------ Test 1 ------------------")
    print("Testing the search algorithms on first problem instance (running time may not be better for AStar Search):")
    sanity = test_grid(1, print_route=True)
    print("First problem instance passed? ", sanity)

    print("------------------ Test 2 ------------------")
    print("Testing the search algorithms on the second problem instance (running time should be better for AStar Search):")
    sanity = test_grid(2)
    print("Second problem instance passed? ", sanity)

if __name__ == "__main__":
    run_tests()