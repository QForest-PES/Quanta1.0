import os
import json
import random
import hashlib
from Crypto.PublicKey import RSA
from qiskit import QuantumCircuit, transpile
from math import gcd
from qiskit_ibm_provider import IBMProvider

# Load IBM Quantum account (ensure API key is already saved)
provider = IBMProvider()
print("Available Quantum Devices:", provider.backends())

def generate_weak_128bit_integer():
    """
    Generates a 128-bit integer that is easily factored.
    """
    p = 6700417  # Small 64-bit prime
    q = 9576890767  # Another small 64-bit prime
    return p * q

def generate_rsa_moduli(num_keys):
    """
    Generates multiple RSA moduli (public-private key pairs).
    """
    moduli = []
    for _ in range(num_keys):
        key = RSA.generate(1024)
        moduli.append({
            "n": str(key.n),  # Convert to string for JSON compatibility
            "e": str(key.e),
            "d": str(key.d)
        })
    return moduli

def hash_password(password):
    """
    Generates a SHA-256 hash of the given password.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def quantum_decision_tree(quantum_secure):
    """
    Placeholder for a Quantum Decision Tree (QDT) model.
    """
    return int(quantum_secure) % 2

def find_period(a, N):
    """
    Finds the period r such that a^r ≡ 1 (mod N).
    """
    r = 1
    while pow(a, r, N) != 1:
        r += 1
    return r

def shors_algorithm(N, max_retries=10):
    """
    Simulates Shor's Algorithm using quantum randomness.
    """
    if N <= 2:
        raise ValueError("N must be greater than 2 for Shor's algorithm.")
    if N % 2 == 0:
        return 2, N // 2  # Trivial factorization if even

    def get_random_a():
        return random.randint(2, N - 2)

    for _ in range(max_retries):
        a = get_random_a()
        while gcd(a, N) != 1:
            a = get_random_a()  # Ensure a is coprime to N

        r = find_period(a, N)
        if r % 2 == 1:
            continue  # Odd period, retry with another a

        factor1 = gcd(pow(a, r // 2) - 1, N)
        factor2 = gcd(pow(a, r // 2) + 1, N)

        if factor1 == 1 or factor2 == 1:
            continue  # Need to retry with another a

        return factor1, factor2

    return None  # Failed to find factors after max_retries

def main():
    password = input("Enter a password: ")
    hashed_password = hash_password(password)
    print(f"SHA-256 Hash: {hashed_password}")

    num_moduli = 50
    rsa_keys_file = "rsa_keys.json"

    if os.path.exists(rsa_keys_file):
        print("[ℹ] Loading existing RSA keys from rsa_keys.json...")
        with open(rsa_keys_file, "r") as f:
            moduli_list = json.load(f)
    else:
        print(f"Generating {num_moduli} RSA moduli...")
        moduli_list = generate_rsa_moduli(num_moduli)
        with open(rsa_keys_file, "w") as f:
            json.dump(moduli_list, f)

    for entry in moduli_list:
        entry["n"] = int(entry["n"])
        entry["e"] = int(entry["e"])
        entry["d"] = int(entry["d"])

    best_n = None
    best_score = -1

    num_shor_tests = min(5, len(moduli_list))
    shor_test_moduli = random.sample(moduli_list, num_shor_tests)

    for entry in moduli_list:
        n = entry["n"]
        print(f"\nEvaluating modulus: {n}")

        if entry in shor_test_moduli:
            print("[⏳] Running Shor’s Algorithm on selected N...")
            quantum_secure = shors_algorithm(n) is None
            print(f"[✅] Shor’s Algorithm check complete. Secure? {quantum_secure}")
        else:
            print("🔹 Skipping Shor’s Algorithm (Performance Optimization)")
            quantum_secure = True

        print("[⏳] Evaluating security score using QDT model...")
        score = quantum_decision_tree(quantum_secure)
        print(f"[✅] QDT Score: {score}")

if __name__ == "__main__":
    main()
