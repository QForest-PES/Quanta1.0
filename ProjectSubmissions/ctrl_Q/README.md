# Quantum Random Password Generator

This project demonstrates a quantum random password generator using Qiskit. The quantum circuit generates randomness, which is then used to create a secure password.

## Project Overview

- **Quantum Randomness**: Utilizes qubits to ensure the randomness of the generated passwords.
- **Character Set Options**: Supports various character sets including uppercase, lowercase, digits, and special characters.
- **High Security**: Generates passwords that are highly secure and resistant to common attacks.

## Prerequisites

To run this project, you need to have a quantum computing environment set up. We recommend using Qiskit, an open-source quantum computing framework.

1. Install Qiskit:
    ```bash
    pip install qiskit
    ```

2. Install Matplotlib for circuit visualization:
    ```bash
    pip install matplotlib
    ```


## Usage

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/quantum-password-generator.git
    cd quantum-password-generator
    ```

2. Run the script:
    ```bash
    python sourcecode.py
    ```

## Code Explanation

### Quantum Circuit

The quantum circuit is created with 8 qubits, and Hadamard gates are applied to create superposition. All qubits are then measured to generate randomness.

```python
qc = QuantumCircuit(8)
qc.h(range(8))  # Apply Hadamard gates to create superposition
qc.measure_all()  # Measure all qubits
```

### Password Generation

The password is generated using a combination of uppercase letters, lowercase letters, digits, and special characters. The function ensures that the password contains at least one uppercase letter and one special character.

```python
def generate_password():
    while True:
        password = ''.join(random.choice(characters) for _ in range(8))
        if any(c in uppercase for c in password) and any(c in special_chars for c in password):
            return password
```

### Output

The generated password is printed to the console.

```python
password = generate_password()
print("Quantum-Generated Password:", password)
```


## Contact

For any questions or suggestions, please contact us 
Krish: reachkrishmathur@gmail.com
Sonia: xsoniaaaxx@gmail.com
