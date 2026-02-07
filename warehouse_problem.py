from Algorithms_updated import Problem

class WarehouseRobotProblem(Problem):
    """
    Class to represent the Warehouse Robot Problem.

    Author: Mahtabin Tushi
    Date: 2026-01-29
    Sources: Custom implementation based on the warehouse navigation problem
    """

    def __init__(self, grid, start, goal):
        """
        Store grid, start, and goal positions.
        """
        super().__init__(start)
        self.grid = grid
        self.goal = goal

    def is_goal(self, state):
        """
        Goal test: robot reaches the goal cell.
        """
        return state == self.goal

    def next_states(self, state):
        """
        Return list of (action, next_state) for valid moves.
        Movement allowed: up, down, left, right.
        """
        r, c = state
        rows = len(self.grid)
        cols = len(self.grid[0])

        directions = {
            "up":    (r - 1, c),
            "down":  (r + 1, c),
            "left":  (r, c - 1),
            "right": (r, c + 1),
        }

        result = []
        for action, (nr, nc) in directions.items():
            if 0 <= nr < rows and 0 <= nc < cols:
                if isinstance(self.grid[nr][nc], (int, float)):
                    result.append((action, (nr, nc)))

        return result

    def g(self, state):
        """
        Step cost: terrain weight of the cell being entered.
        Used by UCS and A*.
        """
        r, c = state
        return self.grid[r][c]

    def h(self, state):
        """
        Heuristic: Manhattan distance to goal.
        Used by Greedy Best-First and A*.
        """
        r, c = state
        gr, gc = self.goal
        return abs(gr - r) + abs(gc - c)