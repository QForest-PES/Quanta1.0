**Quantum CAPTCHA System 🔐⚛️**  
**Quantum-Powered CAPTCHA** system that enhances security using **Qiskit's quantum randomness**, **ASCII obfuscation**, and a **dynamic countdown timer**. This project ensures **human verification** while being resilient against **automated bots**.  

---

✨ Features**
✅ **Quantum-Generated CAPTCHA** – Uses Qiskit to introduce randomness  
✅ **Three Difficulty Levels** – *Easy*, *Medium*, and *Hard*  
✅ **ASCII-Styled CAPTCHA** – Uses **PyFiglet** to distort text  
✅ **Countdown Timer** – 30 seconds to solve before expiry  
✅ **Multiple Attempts** – 3 retries before lockout  
✅ **Case-Sensitive & Symbol-Sensitive** – More security against bots  
✅ **Auto-Screen Clearing** – Improves readability  

---

## **🚀 How It Works**
1️⃣ Generates a **random CAPTCHA** (letters, numbers, symbols)  
2️⃣ Passes characters through a **quantum circuit** (Qiskit)  
3️⃣ Uses **Quantum Superposition & Measurement** to modify text  
4️⃣ Displays **ASCII-stylized CAPTCHA** for distortion  
5️⃣ Starts a **countdown timer** (30 seconds)  
6️⃣ **User inputs CAPTCHA** → Verified against expected output  
7️⃣ **Success? ✅** – Pass granted! 🎉  
8️⃣ **Fail or Timeout? ❌** – New CAPTCHA generated (3 attempts max)  

---

🛠️ Installation**
1️⃣ Install Dependencies**

pip install qiskit qiskit-aer pyfiglet colorama



2️⃣ Run the Program**
python quantum_captcha.py

---

## **📌 Dependencies**
- **Qiskit** – Quantum computing library for randomness  
- **Qiskit AerSimulator** – Simulates quantum circuits  
- **Colorama** – Adds terminal colors  
- **PyFiglet** – Converts text into ASCII art  
- **Threading** – Runs countdown alongside user input  
- **Time & Sys** – Manages countdown and display  

---

🖥️ Difficulty Modes**
🔹 Easy → Letters (A-Z) + Digits (0-9)  
🔹 Medium → Letters (A-Z, a-z) + Digits  
🔹 Hard → Letters + Digits + Special Characters (**@#$%&*!?**)  




🔒 Security Enhancements**
✔ Quantum-Based Variability** – Harder to predict patterns  
✔ Case-Sensitive & Symbol-Sensitive** – Strengthens verification  
✔ Limited Attempts** – Prevents brute-force attacks  
✔ Obfuscation with ASCII Fonts** – Harder for bots to read  





