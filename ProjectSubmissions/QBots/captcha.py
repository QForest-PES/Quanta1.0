import random
import string
import time
import sys
import threading
import os
import errno
import pyfiglet  # Added for ASCII CAPTCHA fonts
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from colorama import Fore, Style, init

# Initialize colorama for colored text support
init(autoreset=True)

def clear_screen():
    """Clears the screen for both Windows and Unix-based systems."""
    os.system("cls" if os.name == "nt" else "clear")

def generate_random_character(difficulty):
    """Generate a random character based on difficulty level."""
    if difficulty == 'easy':
        characters = string.ascii_uppercase + string.digits  # A-Z, 0-9
    elif difficulty == 'medium':
        characters = string.ascii_letters + string.digits  # A-Z, a-z, 0-9
    else:
        characters = string.ascii_letters + string.digits + "@#$%&*?!"
    return random.choice(characters)

def generate_quantum_captcha(difficulty='medium'):
    """Generates a quantum CAPTCHA challenge using Qiskit."""
    captcha_length = 6 if difficulty == 'easy' else 8 if difficulty == 'medium' else 10
    captcha = "".join(generate_random_character(difficulty) for _ in range(captcha_length))

    qc = QuantumCircuit(captcha_length, captcha_length)
    for i in range(captcha_length):
        char_value = ord(captcha[i]) % 4
        if char_value == 1:
            qc.x(i)
        elif char_value == 2:
            qc.h(i)
        elif char_value == 3:
            qc.x(i)
            qc.h(i)
        elif char_value == 0 and difficulty == 'hard':
            qc.z(i)  # Add extra randomness for hard mode

    qc.measure(range(captcha_length), range(captcha_length))
    simulator = AerSimulator()
    job = simulator.run(qc, shots=1)
    result = job.result()
    quantum_outcomes = list(result.get_counts().keys())[0]
    quantum_outcomes = quantum_outcomes.zfill(captcha_length)

    new_captcha = "".join(
        captcha[i].lower() if quantum_outcomes[i] == "1" and captcha[i].isalpha() else captcha[i]
        for i in range(captcha_length)
    )

    # Use PyFiglet to make the CAPTCHA harder to read
    fonts = ["slant", "shadow", "3d", "block", "small", "smslant"]  # Random font choices
    selected_font = random.choice(fonts)
    ascii_captcha = pyfiglet.figlet_format(new_captcha, font=selected_font)

    clear_screen()
    print(Fore.CYAN + "\n--- Quantum CAPTCHA ---")
    print(Fore.YELLOW + f"Generated CAPTCHA (Expires in 40 seconds!):\n")
    print(Fore.GREEN + ascii_captcha)  # Display ASCII-styled CAPTCHA

    return new_captcha

def countdown_timer(timeout):
    """Handles the countdown timer separately using threading."""
    global time_up
    for remaining_time in range(timeout, 0, -1):
        if time_up:
            return
        sys.stdout.write(Fore.BLUE + f"\r⏳ Time left: {remaining_time} seconds  ")
        sys.stdout.flush()
        time.sleep(1)
    time_up = True
    sys.stdout.write("\r" + " " * 50 + "\r")

def verify_user_response(expected_captcha, timeout=30, attempts_left=3):
    """Verifies if the user's response matches the generated CAPTCHA within the time limit."""
    global time_up
    time_up = False

    print(Fore.MAGENTA + "⚡ Type the CAPTCHA exactly as shown. Case & special characters matter!")
    print(Fore.LIGHTWHITE_EX + "You have 30 seconds to enter the CAPTCHA below:\n")

    timer_thread = threading.Thread(target=countdown_timer, args=(timeout,))
    timer_thread.start()

    user_input = input_with_timeout(Fore.LIGHTWHITE_EX + "✍ Enter CAPTCHA: ", timeout)
    time_up = True
    timer_thread.join()

    if user_input is None:
        clear_screen()
        print(Fore.RED + f"\n❌ You ran out of time! You have {attempts_left - 1} more chances.\n")
        return False

    if user_input == expected_captcha:
        clear_screen()
        print(Fore.GREEN + "✅ CAPTCHA solved correctly! You are human. 🎉\n")
        return True

    print(Fore.RED + "❌ Incorrect CAPTCHA! Try again.\n")
    return False

def input_with_timeout(prompt, timeout):
    """Handles user input with a timeout, removing input option after failure."""
    global time_up
    user_input = [None]

    def get_input():
        try:
            user_input[0] = input(prompt).strip()
        except EOFError:
            pass
        time_up = True

    input_thread = threading.Thread(target=get_input)
    input_thread.start()
    input_thread.join(timeout)

    if input_thread.is_alive():
        time_up = True
        clear_screen()
        return None

    return user_input[0]

def run_captcha_system(difficulty='medium'):
    """Runs the Quantum CAPTCHA system with retries."""
    attempts = 3

    while attempts > 0:
        expected_captcha = generate_quantum_captcha(difficulty)
        if verify_user_response(expected_captcha, attempts_left=attempts):
            return "CAPTCHA solved!"

        attempts -= 1
        if attempts == 0:
            clear_screen()
            print(Fore.RED + "\n🚨 Too many failed attempts! Access Locked. 🚨\n")
            return "Access locked due to failed CAPTCHA attempts."

        print(Fore.YELLOW + f"\n🔄 You have {attempts} attempts left. Generating a new CAPTCHA...\n")
        time.sleep(2)

# Example Run
if __name__ == "__main__":
    run_captcha_system('medium')
