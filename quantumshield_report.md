# QuantumShield Security Report

**Generated:** 2025-11-26 04:50:52 UTC

Author: **Ndeleh**

## Overview

This report summarizes cryptographic assets discovered on the system and evaluates their risk in the context of future quantum computers.

## Summary of Findings

- Total cryptographic items found: **40**
- High quantum risk: **3**
- Medium quantum risk: **0**
- Low quantum risk: **0**

## Detailed Findings

### Finding 1

- **Component:** SSH Host Key
- **File:** `/etc/ssh/ssh_host_ed25519_key.pub`
- **Algorithm:** ED25519
- **Combined Quantum Risk:** **High**

**Explanation:** Uses Ed25519; not directly broken by current quantum attacks but long-term risk remains.

---

### Finding 2

- **Component:** SSH Host Key
- **File:** `/etc/ssh/ssh_host_ecdsa_key.pub`
- **Algorithm:** ECDSA
- **Combined Quantum Risk:** **High**

**Explanation:** Uses ECC, which is also vulnerable to Shor's quantum algorithm.

---

### Finding 3

- **Component:** SSH Host Key
- **File:** `/etc/ssh/ssh_host_rsa_key.pub`
- **Algorithm:** RSA
- **Combined Quantum Risk:** **High**

**Explanation:** Uses RSA, which is vulnerable to Shor's quantum algorithm.

---

### Finding 4

- **Component:** SSH Config
- **File:** `/etc/ssh/sshd_config`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 5

- **Component:** SSH Config
- **File:** `/etc/ssh/ssh_config`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 6

- **Component:** Config File
- **File:** `/etc/nanorc`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 7

- **Component:** Config File
- **File:** `/etc/mime.types`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 8

- **Component:** Config File
- **File:** `/etc/services`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 9

- **Component:** Config File
- **File:** `/etc/ca-certificates.conf`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 10

- **Component:** Config File
- **File:** `/etc/protocols`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 11

- **Component:** Config File
- **File:** `/etc/cloud/templates/chrony.conf.freebsd.tmpl`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 12

- **Component:** Config File
- **File:** `/etc/ssl/certs/93bc0acc.0`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 13

- **Component:** Config File
- **File:** `/etc/ssl/certs/6fa5da56.0`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 14

- **Component:** Config File
- **File:** `/etc/ssl/certs/DigiCert_Assured_ID_Root_G3.pem`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 15

- **Component:** Config File
- **File:** `/etc/ssl/certs/SSL.com_Root_Certification_Authority_RSA.pem`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 16

- **Component:** Config File
- **File:** `/etc/ssl/certs/7f3d5d1d.0`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 17

- **Component:** Config File
- **File:** `/etc/ssl/certs/ca-certificates.crt`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 18

- **Component:** Config File
- **File:** `/etc/ssl/certs/AffirmTrust_Networking.pem`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 19

- **Component:** Config File
- **File:** `/etc/ssh/sshd_config`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 20

- **Component:** Config File
- **File:** `/etc/ssh/ssh_config`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 21

- **Component:** Config File
- **File:** `/etc/ssh/ssh_host_ecdsa_key.pub`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 22

- **Component:** Config File
- **File:** `/etc/ssh/ssh_host_rsa_key.pub`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 23

- **Component:** Config File
- **File:** `/etc/alternatives/ex`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 24

- **Component:** Config File
- **File:** `/etc/alternatives/liblapack.so.3-x86_64-linux-gnu`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 25

- **Component:** Config File
- **File:** `/etc/alternatives/infobrowser`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 26

- **Component:** Config File
- **File:** `/etc/alternatives/nodejs`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 27

- **Component:** Config File
- **File:** `/etc/alternatives/vim`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 28

- **Component:** Config File
- **File:** `/etc/alternatives/c++`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 29

- **Component:** Config File
- **File:** `/etc/alternatives/vimdiff`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 30

- **Component:** Config File
- **File:** `/etc/alternatives/cpp`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 31

- **Component:** Config File
- **File:** `/etc/alternatives/rvim`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 32

- **Component:** Config File
- **File:** `/etc/alternatives/view`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 33

- **Component:** Config File
- **File:** `/etc/alternatives/lzcat`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 34

- **Component:** Config File
- **File:** `/etc/alternatives/editor`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 35

- **Component:** Config File
- **File:** `/etc/alternatives/cc`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 36

- **Component:** Config File
- **File:** `/etc/alternatives/lzma`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 37

- **Component:** Config File
- **File:** `/etc/alternatives/unlzma`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 38

- **Component:** Config File
- **File:** `/etc/alternatives/rview`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 39

- **Component:** Config File
- **File:** `/etc/alternatives/vi`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

### Finding 40

- **Component:** Config File
- **File:** `/etc/alternatives/pico`
- **Algorithm:** Unknown
- **Combined Quantum Risk:** **Unknown**

**Explanation:** Potential cryptographic material found; evaluate for quantum safety.

---

## Recommended Next Steps

- Prioritize migration away from RSA and ECC towards post-quantum algorithms.
- Inventory all externally-facing services using vulnerable algorithms.
- Follow NIST post-quantum cryptography guidance when selecting replacements.
