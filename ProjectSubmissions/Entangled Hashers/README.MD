# N-Queens Solver

## Overview
This project is an implementation of the **N-Queens Problem**, a classic combinatorial problem in which the goal is to place **N queens** on an **N × N chessboard** such that no two queens threaten each other. This means:

- No two queens share the same **row**.
- No two queens share the same **column**.
- No two queens share the same **diagonal**.

The project provides an efficient solution using **backtracking** and other optimization techniques.

## Features
- Solves the N-Queens problem for any given **N**.
- Displays the chessboard with queen placements.
- Allows visualization of solutions.
- Supports optimization techniques to reduce backtracking steps.

## Installation
### Prerequisites
Ensure you have the following installed:
- **Python 3.x**
- **Jupyter Notebook** (optional, for running `.ipynb` files)

### Setup
Clone the repository:
```sh
$ git clone <repository-url>
$ cd N-queens
```

Install dependencies:
```sh
$ pip install -r requirements.txt
```

## Usage
### Running the Solver
To execute the solver, run the Jupyter Notebook:
```sh
$ jupyter notebook N-queens.ipynb
```
Follow the instructions inside the notebook to solve for different values of **N**.

### Example Output
For **N = 4**, one possible solution:
```
. Q . .
. . . Q
Q . . .
. . Q .
```

## Explanation of the Algorithm
The backtracking algorithm follows these steps:
1. Place a queen in the first available column of a row.
2. Move to the next row and repeat.
3. If no valid position is found, **backtrack** to the previous row and move the queen.
4. Repeat until all queens are placed successfully.

## Future Improvements
- Implement **heuristic-based approaches** (e.g., genetic algorithms, constraint programming).
- Optimize performance for large **N** values.
- Develop a **graphical visualization**.

## License
This project is licensed under the **MIT License**.

## Acknowledgments
- The N-Queens problem is a fundamental topic in **Artificial Intelligence** and **Combinatorial Optimization**.
- Inspired by various algorithmic approaches in competitive programming and academic research.

---

Happy Coding! 🚀

