### Project by:
- Rachna Nayak
- Anvi Jain <br>

Email: rachnaammunjenayak@gmail.com

### Summary:
This code utilizes quantum computing to generate a random permutation of seats for students. It uses the Fisher-Yates shuffle algorithm, but instead of relying on classical randomness, it leverages quantum randomness to shuffle the seats.

This ensures that no bias occurs in the shuffling process, making it ideal for applications where fairness is crucial, like while assigning students to terminals for exams. 

### Functions:
- quantum_shuffle(num_students)
    - Generates a random permutation of seats for students using quantum computing.
    - input parameters: number of students to be assigned seats
    - output: A list where the index is the student number and the value is the assigned seat
    - This function initializes a list of seat assignments, then performs a quantum-based Fisher-Yates shuffle to randomize the assignments

- quantum_random_number(max_value)
    - Generates a quantum random number between 0 and max_value - 1.
    - input parameters: the max value that the random number can take
    - output: random integer between 0 and max_value - 1
    - This function calculates the required number of qubits based on max_value, creates a quantum circuit, applies Hadamard gates to put qubits in superposition, measures the qubits, and returns the resulting random number.
    - it uses a time based seed to get multiple, unique runs each time

### What is Happening Here? 
- Based on the number of students given as input by the user, the appropriate number of qubits are initialised.
- quantum_shuffle initialises the list of seat arrangements and does a quantum-based Fisher-Yates shuffle
    - The Fisher-Yates shuffle is a method for generating a random permutation of a finite sequence in O(n) time
    - The quantum version of this algorithm uses the quantum random number generator to generate the random numbers required
- a quantum circuit is used to generate the random numbers
- each qubit is put into superposition using Hadamard Gates
- then, the set of qubits are measured, causing them to collapse into either |1> or |0>, generating random binary strings
- the binary strings are then converted into integers, which may be out of the range of needed values, in which case we use the % (mod) operation to get a random value within the needed range.

### Important Concepts:
- Quantum Superposition: The ability of a qubit to exist in multiple states simultaneously.
- Hadamard Gate: A quantum gate that puts a qubit into a superposition state.
- Quantum Measurement: The process of collapsing a qubit's superposition state into a single outcome.
- Fisher-Yates Shuffle: A classical algorithm for generating a random permutation of a list.
