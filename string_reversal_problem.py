from Algorithms_updated import Problem

class StringReversalProblem(Problem):
    """
    Class to represent the String Reversal Problem.

    Author: Mahtabin Tushi
    Date: 2026-01-29
    Sources: Custom implementation for string sorting by reversal
    """

    def __init__(self, start, goal):
        """
        Store start and goal strings.
        """
        super().__init__(start)
        self.goal = goal

    def is_goal(self, state):
        """
        Goal test: string matches the goal string.
        """
        return state == self.goal

    def next_states(self, state):
        """
        Return list of (action, next_state) for all substring reversals.
        Action is a tuple (i, j) indicating the reversed substring.
        """
        n = len(state)
        result = []

        for i in range(n):
            for j in range(i + 1, n):
                new_state = state[:i] + state[i:j+1][::-1] + state[j+1:]
                result.append(((i, j), new_state))

        return result

    def g(self, state):
        """
        Cost of a reversal move.
        Each reversal has uniform cost 1.
        """
        return 1

    def h(self, state):
        """
        Heuristic: sum of absolute differences between each character’s
        current index and its index in the goal string.
        """
        distance = 0
        for i, ch in enumerate(state):
            goal_index = self.goal.find(ch)
            if goal_index != -1:
                distance += abs(i - goal_index)
        return distance