from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit_aer import AerSimulator  
import time

def quantum_shuffle(num_students):
    """
    Uses quantum computing to generate a random permutation of seats for students.
    Returns a list where index is student number and value is assigned seat.
    """
    # Initialize 
    seat_assignments = list(range(num_students))
    
    # Perform a quantum-based Fisher-Yates shuffle
    for i in range(num_students - 1, 0, -1):
        j = quantum_random_number(i + 1)

        seat_assignments[i], seat_assignments[j] = seat_assignments[j], seat_assignments[i]
    
    return seat_assignments

def quantum_random_number(max_value):
    """Generates a quantum random number between 0 and max_value - 1"""
    
    # Calculate required number of qubits based on max_value
    num_qubits = (max_value - 1).bit_length() 

    qreg_q = QuantumRegister(num_qubits, 'q')
    creg_c = ClassicalRegister(num_qubits, 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)
    
    # Apply Hadamard gates to put qubits in superposition
    for i in range(num_qubits):
        circuit.h(qreg_q[i])

    circuit.measure(qreg_q, creg_c)
    
    backend = AerSimulator()
    # Add a small time-based seed to get many unique runs
    seed = int(time.time() * 1000) % 10000 + i  
    job = backend.run(circuit, shots=1, seed_simulator=seed)
    result = job.result()
    
    counts = result.get_counts(circuit)
    binary_result = list(counts.keys())[0]
    
    #get int from binary string of qubits
    random_number = int(binary_result, 2) % max_value
    
    return random_number

num_students = int(input("Enter the number of students: "))
seating_arrangement = quantum_shuffle(num_students)

print("Student to Seat Assignment:")
for student_num, seat_num in enumerate(seating_arrangement):
    print(f"Student {student_num + 1} -> Seat {seat_num + 1}")