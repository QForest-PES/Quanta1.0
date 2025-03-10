# Quantum Digital Signature

This project implements a quantum digital signature (QDS) scheme based on the ideas presented in the paper "[Quantum Digital Signatures](http://arxiv.org/abs/quant-ph/0105032v2)" by Daniel Gottesman and Isaac L. Chuang. The scheme leverages quantum one-way functions to achieve unconditional security in digital signatures, ensuring that a signed message can be verified by multiple recipients while preventing forgery and repudiation.

--------------------------------------------------------------------------------
**SNOWDEN**

**Team Members:**
- Purandar Puneet
- A V Vedanth

**Contact Information:**  
- **Email:** purandarbalasa@gmail.com
--------------------------------------------------------------------------------

## Overview

In classical cryptography, digital signature schemes rely on computationally hard problems. However, with the advent of quantum computing, many of these schemes could become vulnerable. This project implements a quantum digital signature protocol that uses quantum one-way functions to map classical bit strings to quantum states. The protocol ensures that:
- A sender (Alice) can sign a message.
- Multiple recipients can verify the signature.
- Any tampering or forgery is detected with high probability.

## Features

- **Quantum One-Way Functions:** Maps classical bit strings to quantum states that are hard to invert, based on quantum mechanical principles such as the no-cloning theorem and Holevo’s bound.
- **Key Generation:** Generates quantum public keys that are used to verify the signature.
- **Signing Protocol:** Implements the signing procedure where the message is signed using private keys and verified using public keys.
- **Verification:** Uses quantum verification techniques (e.g., the swap test) to ensure the integrity of the message and detect any tampering.

## Prerequisites

Before running the code, ensure you have the following installed:

1. **Python 3.6 or Later**  
   - Download from: [python.org/downloads](https://www.python.org/downloads/)

2. **Cirq**  
   - Required for quantum circuit simulation and quantum operations.  
   - Install via pip:
     ```bash
     pip install cirq
     ```

3. **NumPy**  
   - Used for numerical operations and array handling.  
   - Install via pip:
     ```bash
     pip install numpy
     ```

4. **Standard Python Library Modules**  
   - The code uses the built-in `random` module, which is included with Python.

## Installation & Setup

1. Clone this repository or download the source code or just use Collab.
2. Ensure you have installed the prerequisites mentioned above.
3. Open your terminal or command prompt, navigate to the project directory, and run the code.
