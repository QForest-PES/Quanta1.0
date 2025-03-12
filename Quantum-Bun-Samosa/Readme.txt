# Quantum Maze Solver

## Overview
The Quantum Maze Solver leverages quantum computing principles to navigate and solve a 3x3 maze using quantum walks. By encoding the maze as a graph and utilizing quantum superposition and interference, the algorithm efficiently explores paths to find an optimal solution.

## Problem Statement
Traditional pathfinding algorithms rely on classical computation to traverse a maze. Quantum walks, however, enable simultaneous exploration of multiple paths due to quantum superposition, potentially offering a speedup in maze solving. This project implements a quantum walk-based approach to finding a path through a 3x3 grid maze.

## Implementation Details

### 1. Maze Representation
- The maze is represented as a graph using the `networkx` library.
- Nodes correspond to maze positions (e.g., `(0,0)`, `(1,2)`).
- Edges define valid movements between adjacent cells.

### 2. Quantum Walk Algorithm
- The **position and coin qubits** are used to model movement through the maze.
- **Hadamard gates** initialize an equal superposition of states.
- **Conditional quantum gates** encode the adjacency structure of the maze.
- A **Quantum Fourier Transform (QFT)** enhances probability distribution for solution discovery.
- The system is measured to determine the most probable paths.

### 3. Tools & Libraries Used
- **Qiskit**: For quantum circuit design and execution.
- **NetworkX**: To construct and visualize the maze as a graph.
- **Matplotlib**: For visual representation of the solution path.
- **NumPy**: For matrix operations and probability calculations.

## Code Explanation
The implementation consists of the following steps:
1. **Maze Construction**: A 3x3 grid graph is created using `networkx`.
2. **Quantum Walk Execution**: A quantum circuit simulates movement through the maze.
3. **Measurement & Path Extraction**: The most probable positions are identified and mapped to a path.
4. **Visualization**: The computed solution is displayed using a graph-based approach.

## Results & Insights
- The quantum walk approach distributes probabilities across all possible paths.
- The most probable path represents the shortest or most efficient route through the maze.
- The use of **QFT** improves convergence toward optimal solutions.

## Future Scope
- Extend the solver to larger grid sizes.
- Optimize gate operations for efficiency improvements.
- Implement the algorithm on real quantum hardware using IBM Quantum devices.

## How to Run the Project
1. Install dependencies:
   ```bash
   pip install qiskit networkx matplotlib numpy

## Contributors
- Shubhangi Srivastava
- Souyashvinu Y
- Siddhartha Rao

## Team Name
~ Quantum-bun-samosa ~ 