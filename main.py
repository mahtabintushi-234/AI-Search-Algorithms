"""
main.py
Runs all six search algorithms on both Problem 1 (Warehouse Robot)
and Problem 2 (String Reversal).

Author: Mahtabin Tushi
Date: 2026-01-29
Course: Intro to AI – Search Algorithms
Sources: Assignment instructions  Algorithms_updated.py , Warehouse_Robot provided by instructor.
"""

from Algorithms_updated import bfs, dfs, ucs, greedy_best_first, astar, iddfs
from Warehouse_Robot import generate_weighted_warehouse_board
from warehouse_problem import WarehouseRobotProblem
from string_reversal_problem import StringReversalProblem


# ---------------------------------------------------------
# Problem 1: Warehouse Robot with Weighted Terrain
# ---------------------------------------------------------

def run_warehouse_robot():
    """
    Generate a weighted warehouse board and run all six search algorithms.

    No parameters.
    No return value. Prints results directly.
    """
    board = generate_weighted_warehouse_board(size=8, difficulty="hard", seed=42)
    grid = board["grid"]
    start = board["start"]
    goal = board["goal"]

    problem = WarehouseRobotProblem(grid, start, goal)

    print("=== Problem 1: Warehouse Robot ===")

    print("\nUsing BFS:")
    print(bfs(problem))

    print("\nUsing DFS:")
    print(dfs(problem))

    print("\nUsing IDDFS:")
    print(iddfs(problem))

    print("\nUsing UCS:")
    print(ucs(problem))

    print("\nUsing Greedy Best-First:")
    print(greedy_best_first(problem))

    print("\nUsing A*:")
    print(astar(problem))


# ---------------------------------------------------------
# Problem 2: String Reversal by Substring Reversal
# ---------------------------------------------------------

def run_string_reversal():
    """
    Create a string reversal problem instance and run all six search algorithms.

    No parameters.
    No return value. Prints results directly.
    """
    start_string = "DBCA"
    goal_string = "ABCD"

    problem = StringReversalProblem(start_string, goal_string)

    print("\n=== Problem 2: String Reversal ===")

    print("\nUsing BFS:")
    print(bfs(problem))

    print("\nUsing DFS:")
    print(dfs(problem))

    print("\nUsing IDDFS:")
    print(iddfs(problem))

    print("\nUsing UCS:")
    print(ucs(problem))

    print("\nUsing Greedy Best-First:")
    print(greedy_best_first(problem))

    print("\nUsing A*:")
    print(astar(problem))


# ---------------------------------------------------------
# Main Execution
# ---------------------------------------------------------

if __name__ == "__main__":
    """
    Entry point for running both search problems.
    """
    run_warehouse_robot()
    run_string_reversal()