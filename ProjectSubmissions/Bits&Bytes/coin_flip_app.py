import streamlit as st
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.primitives import Sampler
import random
import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64
import time


# Quantum Coin Flip Protocol Class
class QuantumCoinFlip:
    def __init__(self):

        self.simulator = Aer.get_backend("qasm_simulator")
        self.sampler = Sampler()

    def generate_keypair(self):

        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        public_key = private_key.public_key()
        return private_key, public_key

    def sign_message(self, private_key, message):

        signature = private_key.sign(
            message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256(),
        )
        return base64.b64encode(signature).decode()

    def verify_signature(self, public_key, message, signature):

        try:
            signature_bytes = base64.b64decode(signature)
            public_key.verify(
                signature_bytes,
                message.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH,
                ),
                hashes.SHA256(),
            )
            return True
        except Exception:
            return False

    def create_quantum_circuit(self, seed=None):

        if seed:
            random.seed(seed)

        # Create a quantum circuit with 1 qubit
        qc = QuantumCircuit(1, 1)

        # Apply Hadamard gate to put qubit in superposition
        qc.h(0)

        # Measure the qubit
        qc.measure(0, 0)

        return qc

    def run_circuit(self, circuit, shots=1):

        # Using the new Qiskit primitives API
        job = self.sampler.run(circuit, shots=shots)
        result = job.result()
        # Extract quasi-probabilities from the result
        quasi_dist = result.quasi_dists[0]
        # Convert to traditional counts format
        counts = {
            format(int(key), "0b").zfill(1): val for key, val in quasi_dist.items()
        }
        return counts

    def hash_value(self, value):

        return hashlib.sha256(str(value).encode()).hexdigest()

    def protocol_alice_step1(self, user_seed=None):

        # 1. Generate a random seed or use user input
        if user_seed is not None:
            seed = user_seed
        else:
            seed = random.randint(1, 10000)

        # 2. Create a quantum circuit with this seed
        circuit = self.create_quantum_circuit(seed)

        # 3. Generate a commitment to the seed
        commitment = self.hash_value(seed)

        # 4. Generate keypair for signing
        private_key, public_key = self.generate_keypair()

        # 5. Sign the commitment
        signature = self.sign_message(private_key, commitment)

        return {
            "seed": seed,
            "commitment": commitment,
            "signature": signature,
            "public_key": public_key,
            "circuit": circuit,
        }

    def protocol_bob_step2(
        self, alice_commitment, alice_signature, alice_public_key, user_bit=None
    ):

        # 1. Verify Alice's signature
        if not self.verify_signature(
            alice_public_key, alice_commitment, alice_signature
        ):
            raise ValueError("Invalid signature from Alice")

        # 2. Bob generates his own random bit or uses user input
        if user_bit is not None and user_bit in [0, 1]:
            bob_bit = user_bit
        else:
            bob_bit = random.randint(0, 1)

        # 3. Generate keypair for signing
        private_key, public_key = self.generate_keypair()

        # 4. Sign the bit
        signature = self.sign_message(private_key, str(bob_bit))

        return {"bob_bit": bob_bit, "signature": signature, "public_key": public_key}

    def protocol_alice_step3(self, bob_bit, bob_signature, bob_public_key, alice_data):

        # 1. Verify Bob's signature
        if not self.verify_signature(bob_public_key, str(bob_bit), bob_signature):
            raise ValueError("Invalid signature from Bob")

        # 2. Reveal the seed
        seed = alice_data["seed"]

        # 3. Verify that the commitment matches the seed
        if self.hash_value(seed) != alice_data["commitment"]:
            raise ValueError("Commitment doesn't match seed")

        # 4. Run the quantum circuit with Alice's seed
        counts = self.run_circuit(alice_data["circuit"])

        # 5. Extract the measurement result (0 or 1)
        alice_bit = 0 if "0" in counts else 1

        # 6. Combine Alice's quantum bit with Bob's bit for final result
        # XOR the bits for the final result
        final_result = alice_bit ^ bob_bit

        return {"alice_bit": alice_bit, "seed": seed, "final_result": final_result}

    def protocol_bob_verify(self, alice_seed, alice_commitment, alice_bit):

        # 1. Verify that the commitment matches the seed
        if self.hash_value(alice_seed) != alice_commitment:
            return False

        # 2. Recreate the quantum circuit with Alice's seed
        circuit = self.create_quantum_circuit(alice_seed)

        # 3. Run the quantum circuit to verify the result
        counts = self.run_circuit(circuit)

        # 4. Extract the measurement result (0 or 1)
        verified_bit = 0 if "0" in counts else 1

        # 5. Check if the verified bit matches Alice's claimed bit
        return verified_bit == alice_bit


# Streamlit App
def main():
    st.title(" 🪙 Quantum Coin Flip Protocol")
    st.sidebar.title("Navigation")
    choice = st.sidebar.radio(
        "Choose an option:", ["Automatic Protocol", "Interactive Protocol", "About"]
    )

    qcf = QuantumCoinFlip()

    if choice == "Automatic Protocol":
        st.header("Automatic Quantum Coin Flip Protocol")
        if st.button("Run Automatic Protocol"):
            with st.spinner("Running protocol..."):
                result = run_complete_protocol(qcf)
                st.success(
                    f"Final coin flip result: {'Heads' if result == 0 else 'Tails'}"
                )

    elif choice == "Interactive Protocol":
        st.header("Interactive Quantum Coin Flip Protocol")
        run_interactive_protocol(qcf)

    elif choice == "About":
        st.header("About")
        st.write("This is a Streamlit app for the Quantum Coin Flip Protocol.")
        st.write(
            "The protocol simulates a fair coin flip between two parties using quantum mechanics."
        )


def run_complete_protocol(qcf):
    st.write("Running automatic quantum coin flip protocol...")

    # Alice's step
    alice_data = qcf.protocol_alice_step1()
    st.write(f"Alice's commitment: {alice_data['commitment']}")

    # Bob's step
    bob_data = qcf.protocol_bob_step2(
        alice_data["commitment"], alice_data["signature"], alice_data["public_key"]
    )
    st.write(f"Bob's bit: {bob_data['bob_bit']}")

    # Alice's reveal
    result_data = qcf.protocol_alice_step3(
        bob_data["bob_bit"], bob_data["signature"], bob_data["public_key"], alice_data
    )
    st.write(f"Alice's quantum bit: {result_data['alice_bit']}")
    st.write(f"Alice's seed: {result_data['seed']}")

    # Bob's verification
    is_valid = qcf.protocol_bob_verify(
        result_data["seed"], alice_data["commitment"], result_data["alice_bit"]
    )
    st.write(f"Verification result: {'Valid' if is_valid else 'Invalid'}")

    # Final result
    final_result = result_data["final_result"]
    st.write(f"Final coin flip result: {'Heads' if final_result == 0 else 'Tails'}")

    return final_result


def run_interactive_protocol(qcf):
    st.write("Welcome to the Interactive Quantum Coin Flip Protocol!")
    st.write(
        "This protocol simulates a fair coin flip between two parties using quantum mechanics."
    )

    # Initialize session state
    if "alice_seed" not in st.session_state:
        st.session_state.alice_seed = None
    if "bob_bit" not in st.session_state:
        st.session_state.bob_bit = None
    if "result_data" not in st.session_state:
        st.session_state.result_data = None

    # Get user input for Alice's seed
    user_seed_input = st.radio(
        "Would you like to provide a seed for Alice?",
        ("No", "Yes"),
        key="alice_seed_radio",
    )
    if user_seed_input == "Yes":
        st.session_state.alice_seed = st.number_input(
            "Enter a seed (an integer):", min_value=1, value=42, key="alice_seed_input"
        )
        st.write(f"Using your seed: {st.session_state.alice_seed}")
    else:
        st.session_state.alice_seed = None
        st.write("Using a random seed for Alice.")

    # Alice creates a quantum circuit with the seed
    st.write("\n1. Alice creates a quantum circuit with a seed and commits to it")
    alice_data = qcf.protocol_alice_step1(st.session_state.alice_seed)
    st.write(f"   Alice's commitment: {alice_data['commitment']}")

    # Get user input for Bob's bit
    user_bit_input = st.radio(
        "Would you like to provide Bob's bit?", ("No", "Yes"), key="bob_bit_radio"
    )
    if user_bit_input == "Yes":
        st.session_state.bob_bit = st.number_input(
            "Enter Bob's bit (0 or 1):",
            min_value=0,
            max_value=1,
            value=0,
            key="bob_bit_input",
        )
        st.write(f"Using your bit: {st.session_state.bob_bit}")
    else:
        st.session_state.bob_bit = None
        st.write("Using a random bit for Bob.")

    # Bob provides his random bit
    st.write("\n2. Bob receives Alice's commitment and provides his random bit")
    bob_data = qcf.protocol_bob_step2(
        alice_data["commitment"],
        alice_data["signature"],
        alice_data["public_key"],
        st.session_state.bob_bit,
    )
    st.write(f"   Bob's bit: {bob_data['bob_bit']}")

    # Alice reveals her seed and runs the quantum circuit
    st.write("\n3. Alice reveals her seed and runs the quantum circuit")
    st.session_state.result_data = qcf.protocol_alice_step3(
        bob_data["bob_bit"], bob_data["signature"], bob_data["public_key"], alice_data
    )
    st.write(f"   Alice's quantum bit: {st.session_state.result_data['alice_bit']}")
    st.write(f"   Alice's seed: {st.session_state.result_data['seed']}")

    # Bob verifies Alice's reveal
    st.write("\n4. Bob verifies Alice's reveal")
    is_valid = qcf.protocol_bob_verify(
        st.session_state.result_data["seed"],
        alice_data["commitment"],
        st.session_state.result_data["alice_bit"],
    )
    st.write(f"   Verification result: {'Valid' if is_valid else 'Invalid'}")

    # Final result
    st.write("\n5. Final coin flip result")
    st.write(
        f"   Alice's bit ⊕ Bob's bit = {st.session_state.result_data['alice_bit']} ⊕ {bob_data['bob_bit']} = {st.session_state.result_data['final_result']}"
    )
    st.write(
        f"   Result: {'Heads' if st.session_state.result_data['final_result'] == 0 else 'Tails'}"
    )

    # Ask if user wants to flip again
    if st.button("Flip Again", key="flip_again_button"):
        # Reset the session state for a new flip
        st.session_state.alice_seed = None
        st.session_state.bob_bit = None
        st.session_state.result_data = None
        st.experimental_rerun()  # Rerun the app to reset the inputs


if __name__ == "__main__":
    main()
