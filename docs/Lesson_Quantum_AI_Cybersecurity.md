# Lesson: Quantum Computing, AI, and the Future of Cybersecurity

**Author:** Ndeleh  

---

## 1. Learning Objectives

By the end of this lesson, you will be able to:

1. Explain the basic concepts of **quantum computing** (qubits, superposition, entanglement).
2. Describe how **quantum computing and AI** can work together.
3. Understand why quantum computing is a serious **threat to modern cryptography**.
4. Run and interpret results from **QuantumShield**, a quantum-vulnerability scanner.
5. Propose **mitigation strategies** using post-quantum cryptography.

---

## 2. Background: What is Quantum Computing?

Traditional computers use **bits**:
- A bit can be either `0` or `1`.

Quantum computers use **qubits**:
- A qubit can be in a **superposition** of `0` and `1` at the same time.
- Qubits can be **entangled**, meaning the state of one qubit is linked to the state of another, even at a distance.

These properties allow quantum computers to:
- Explore many possibilities in parallel.
- Solve some problems much faster than classical computers.

### Important Concepts

- **Superposition** – a qubit can be both `0` and `1` until measured.
- **Entanglement** – qubits share a linked state; measuring one affects the other.
- **Interference** – quantum states can combine to amplify correct answers and cancel out incorrect ones.

---

## 3. Quantum Computing + AI: A Powerful Combination

**AI** (Artificial Intelligence) already helps with:
- Pattern recognition
- Anomaly detection
- Prediction and optimization

**Quantum AI** combines AI with quantum computing to:
- Train models faster on large datasets.
- Search through huge solution spaces.
- Potentially detect cyber threats in real time.

### Potential Benefits

- Faster anomaly detection in networks.
- Better optimization of security controls.
- Faster cryptanalysis for defensive research.

### Potential Risks

- AI-guided **quantum attacks** could:
  - Break encryption more efficiently.
  - Design advanced malware.
  - Discover weaknesses in protocols at scale.

---

## 4. Why Quantum Computing Threatens Cybersecurity

Modern cryptography relies on math problems that are **hard for classical computers**.

Examples:

- **RSA** – security is based on the difficulty of factoring large numbers.
- **ECC (Elliptic Curve Cryptography)** – security is based on the elliptic curve discrete logarithm problem.

A powerful enough quantum computer running **Shor’s Algorithm** could:
- Factor large numbers efficiently.
- Break RSA and ECC-based schemes.

This means:

- Encrypted communications could be decrypted.
- VPNs and secure web traffic could be exposed.
- Digital signatures could be forged.
- Long-term secrets (government, health, financial data) are at risk.

### Y2Q – The “Quantum Apocalypse”

**Y2Q** is a term used for the moment when quantum computers become powerful enough to break today’s widely deployed cryptography.

Even if that day is in the future, attackers can:
- Capture encrypted traffic **now**.
- Decrypt it later once they have quantum capabilities (“**harvest now, decrypt later**”).

---

## 5. Real-World Problem

> Organizations today are still heavily dependent on **RSA** and **ECC**.  
> Many don’t even know where these algorithms are used in their systems.

Without visibility, they cannot plan a move to **post-quantum cryptography (PQC)**.

This creates a realistic and urgent problem:

> “How can we quickly scan a Linux system to identify cryptographic assets that might be vulnerable to future quantum attacks?”

---

## 6. Project: QuantumShield – Quantum Vulnerability Scanner

To address this problem, this lesson uses a practical project:

### Project Name

**QuantumShield** – a Python-based tool that runs on Linux and:

- Scans for cryptographic assets (SSH keys, configs, certificates).
- Detects usage of **RSA**, **ECC**, and other algorithms.
- Classifies quantum risk levels (High/Medium/Low).
- Generates a **Markdown report** summarizing findings and suggesting next steps.

This project is both:
- A **learning tool** for quantum-related security concepts.
- A **portfolio project** suitable for GitHub.

---

## 7. Technical Overview of QuantumShield

### 7.1 What QuantumShield Scans

- **SSH Host Keys** in `/etc/ssh`
  - Detects algorithms like RSA, ECDSA, ED25519.
- **SSH Config Files**
  - Looks for references to RSA/ECDSA.
- **Certificates (X.509)**
  - Uses `openssl` to read the public key algorithm and signature algorithm.
- **Generic Config Files under `/etc`**
  - Searches for mentions of RSA or ECDSA as a rough heuristic.

### 7.2 How Risk is Classified

QuantumShield uses simple rule-based logic:

- If algorithms like **RSA**, **ECC**, **ECDSA** are found:
  - Risk is usually classified as **High** (quantum vulnerable).
- If **Ed25519** is used:
  - Risk may be considered **Medium** (not broken like RSA/ECC, but future risks exist).
- If post-quantum algorithms (like Dilithium, Falcon, Kyber) were detected:
  - They would generally be classified as **Low** (future resistant).

The logic is kept transparent so learners can read, modify, and extend it.

---

## 8. Hands-On Lab Instructions (Linux)

### 8.1 Prerequisites
