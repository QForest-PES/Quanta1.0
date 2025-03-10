# Quantum Coin Flip Protocol

## Overview :

This project implements a **Quantum Coin Flip Protocol** using Streamlit and Qiskit. The protocol simulates a fair coin flip between two parties, Alice and Bob, leveraging quantum mechanics to ensure fairness and security. The project is designed to demonstrate how quantum computing can be used in cryptographic protocols to achieve trustless and verifiable outcomes.

The application provides two modes:

-**Automatic Protocol**: Runs the entire protocol automatically without user intervention.  

-**Interactive Protocol**: Allows users to interactively participate in the protocol by providing inputs for Alice's seed and Bob's bit.

## Features :

- **Quantum Circuit Creation**: Uses Qiskit to create and run quantum circuits that simulate a fair coin flip.  

- **Cryptographic Signatures**: Implements RSA-based digital signatures to ensure the integrity and authenticity of the messages exchanged between
  Alice and Bob.  

- **Commitment Scheme**: Uses a cryptographic hash function to create a commitment to Alice's seed, ensuring that Alice cannot change her seed
  after seeing Bob's bit.  

- **Interactive User Interface**: Built with Streamlit, allowing users to interact with the protocol and observe the results in real-time.  

- **Verification Mechanism**: Bob can verify Alice's reveal to ensure that the protocol was executed fairly.  


## How It Works :

**Protocol Steps**

    Alice's Step 1:

        - Alice generates a random seed (or uses a user-provided seed).
        - She creates a quantum circuit using this seed.
        - She generates a commitment to the seed by hashing it.
        - She signs the commitment using her private key and sends the commitment, signature, and public key to Bob.

    Bob's Step 2:

        - Bob verifies Alice's signature on the commitment.
        - Bob generates a random bit (or uses a user-provided bit).
        - He signs his bit using his private key and sends the bit, signature, and public key to Alice.

    Alice's Step 3:

    Alice verifies Bob's signature on his bit.

        - She reveals her seed to Bob.
        - She runs the quantum circuit with her seed to determine her quantum bit.
        - She combines her quantum bit with Bob's bit using XOR to produce the final coin flip result.

    Bob's Verification:

        - Bob verifies that Alice's seed matches the original commitment.
        - He recreates the quantum circuit with Alice's seed and runs it to verify Alice's quantum bit.
        - If the verification is successful, the protocol is considered valid.

**Quantum Circuit :**
The quantum circuit consists of a single qubit. Alice applies a Hadamard gate to the qubit, putting it into a superposition state, and then measures it. The measurement result (0 or 1) is used as Alice's quantum bit.

**Cryptographic Security :**
Digital Signatures: RSA-based signatures are used to ensure that messages from Alice and Bob cannot be tampered with.

**Commitment Scheme:**
The hash of Alice's seed acts as a commitment, ensuring that Alice cannot change her seed after seeing Bob's bit.

**Fairness:**
The protocol ensures that neither Alice nor Bob can influence the outcome of the coin flip after the protocol has started.

## Requirements :

Python 3.7 or higher  
Streamlit  
Qiskit  
Qiskit Aer  
Cryptography library  

## Usage :

**Automatic Protocol:**

- Click the "Run Automatic Protocol" button to execute the entire protocol automatically.
- The final coin flip result will be displayed as either "Heads" or "Tails".

**Interactive Protocol:**

- Choose whether to provide a seed for Alice and a bit for Bob.
- Follow the steps in the protocol as they are displayed on the screen.
- Observe the final coin flip result and verify the protocol's validity.

## Running the Code :

1. Install Dependancies :  

```bash
pip install -r requirements.txt
```

2. Run the CoinFlip App :

```bash
streamlit run coin_flip_app.py
```

