Quantum Walk Simulation

This repository contains a Python implementation of a quantum walk using the Cirq framework. The simulation demonstrates both classical and quantum random walks and visualizes their probability distributions.

Features

Simulates a classical random walk using a biased coin flip.

Computes and visualizes the probability distribution of the classical walk.

Implements a quantum walk using Cirq's quantum circuit simulator.

Uses quantum gates to manipulate qubits and simulate quantum walk behavior.

Graphs the resulting quantum walk probability distribution.

Dependencies

Ensure you have the following Python libraries installed before running the script:

pip install cirq numpy scipy matplotlib

Usage

Run the script to simulate both the classical and quantum walks:

python Quantum_Walk.py

Classical Random Walk

Defined by a probability of stepping right (pr) and a total number of steps (N).

The walker's final position is determined based on weighted coin flips.

Results are visualized as a bar chart.

Quantum Walk

Implemented using a set of qubits and quantum gates.

The walk is executed over a predefined number of iterations (iterator).

Uses Cirq to construct and simulate the quantum circuit.

The final probability distribution is plotted.

File Structure

Quantum_Walk.py - Main script implementing both classical and quantum walk simulations.

Example Output

The script generates probability distributions for both walks and visualizes them using matplotlib. Example graphs include:

Classical random walk histogram.

Quantum walk probability distribution.

License

This project is licensed under the MIT License.

Author

Pulla Jagadeeshwar Reddy
Rahul M Shettigar
Rahul Saran Sharma
