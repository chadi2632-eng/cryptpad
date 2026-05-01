
# Cryptpad CTF Writeup

## Introduction
Hey everyone 👋  
This is my first CTF challenge in reverse engineering.

The challenge is called **Cryptpad**.

---

## Initial Analysis
When opening the binary in a hex editor, I noticed that at the end of the file there are **8 bytes**, which represent the **RC4 key**.

This was an important hint because it suggested that the key is embedded inside the file itself.

---

## Encryption Flow
After analyzing the challenge, I identified the encryption pipeline as:
XOR → RC4 → XOR


This means:
- First layer: XOR encoding
- Second layer: RC4 encryption
- Third layer: XOR encoding again

---

## Implementation
I wrote a Python script to simulate the decryption process.

However, I noticed something interesting:

> When I only applied RC4 decryption, I still got the correct flag.

---

## Observation
This raised a question:
- Either the XOR layers cancel each other out
- Or the XOR operations do not affect the final ciphertext
- Or the RC4 layer is the main effective encryption


