# README  
Intro to Artificial Intelligence – Assignment 1  
Author: **Mahtabin Tushi**  
Date: **2026‑01‑29**

---

# 📌 How to Run the Code

## 1. Python Version
This project requires **Python 3.x**.  
Download it from: https://www.python.org/downloads/

## 2. Installation
No external packages are required.  
All necessary files (`Algorithms_updated.py`, `Warehouse_Robot.py`, etc.) are included in the assignment folder.

## 3. Running the Program
Run the main script:

```bash
python main.py

## Problem 1: Warehouse Robot

### Cost Function `g(state)`

The **cost function** `g(state)` calculates the cost of reaching the current state `(r, c)` in the grid. It is defined as the value stored in the grid at that position. The grid represents terrain with different costs (higher numbers represent higher costs). If the position is out of bounds, the function returns infinity (`float('inf')`), indicating an invalid state.

```python
def g(self, state):
    r, c = state
    if 0 <= r < len(self.grid) and 0 <= c < len(self.grid[0]):
        return self.grid[r][c]
    else:
        return float('inf')
```

### Heuristic Function `h(state)`

The **heuristic function** `h(state)` calculates the **Manhattan distance** between the current state `(r, c)` and the goal position `(goal_r, goal_c)`. This heuristic estimates the distance to the goal by summing the absolute differences in the row and column indices.

```python
def h(self, state):
    r, c = state
    goal_r, goal_c = self.goal
    return abs(goal_r - r) + abs(goal_c - c)
```

This heuristic is **admissible**, meaning it never overestimates the true cost to reach the goal. It is used in the **A*** and **Greedy Best-First** search algorithms.

---

## Problem 2: String Reversal

### Cost Function `g(state)`

In the **String Reversal Problem**, the **cost function** `g(state)` returns the same constant cost for each state, as each string reversal operation (reversing a substring from index `i` to `j`) is treated as having the same cost.

```python
def g(self, state):
    return 1  # Every reversal step has the same cost
```

Here, the cost for every action (reversal) is set to `1`, which simplifies the problem as each step has the same cost.

### Heuristic Function `h(state)`

The **heuristic function** `h(state)` for the string reversal problem measures how far the current string is from the goal string by summing the absolute differences between each character’s current index and its index in the goal string.

```python
def h(self, state):
    distance = 0
    for i in range(len(state)):
        goal_index = self.goal.find(state[i])
        if goal_index != -1:
            distance += abs(i - goal_index)
    return distance
```

 This heuristic estimates how “out of place” each character is.It is **admissible**,  because it never overestimates the number of reversals needed.
---

## Behavioral Comparison: BFS/UCS vs Greedy/A*

### BFS vs UCS

* **BFS** (Breadth-First Search) explores all states level by level, finding the shortest path in terms of the number of steps. It does not consider the cost of the states but only the number of steps needed to reach them.

* **UCS** (Uniform Cost Search) is similar to BFS but takes into account the **actual cost** to reach a state. UCS guarantees finding the least costly path, but it may explore more nodes if the cost of the states varies significantly.

### Greedy Best-First vs A*

* **Greedy Best-First** uses the **heuristic function** to guide the search, always choosing the state that seems closest to the goal according to the heuristic. While it can be faster than A*, it does not guarantee an optimal solution unless the heuristic is perfect.

* **A*** combines both the **actual cost** (`g(state)`) and the **heuristic** (`h(state)`) to make decisions. This makes it more **optimal** than Greedy Best-First, as it considers both past costs and future estimates. However, it may explore more nodes due to the combination of cost and heuristic.

### Key Observations

* **BFS** guarantees the shortest path but might be less efficient in environments with varying costs.
* **UCS** is more cost-efficient but might explore many nodes if the costs are diverse.
* **Greedy Best-First** is faster but might not always find the optimal solution, while **A*** combines optimality with faster convergence.

---

### Final Notes

* Ensure that all dependencies are installed before running the code.
* The **cost functions** and **heuristics** are explained in detail to show how they guide the respective search algorithms.
* A **brief comparison** of the algorithms is provided to explain the behavioral differences between BFS/UCS and Greedy/A*.


