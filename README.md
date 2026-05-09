# File Protection Utility 🔐

A simple Python program that encrypts and decrypts files to keep sensitive data safe. Built as part of an internship task to understand the basics of data protection and controlled access.

---

## What Does It Do?

Ever wondered how apps protect your data? This project does exactly that — it takes a file (like a CSV with grades), locks it into an unreadable format, and can restore it back to its original form whenever needed. Only someone with the correct key can unlock it.

---

## Files in This Project

| File | Description |
|------|-------------|
| `task4.py` | The main Python script |
| `mykey.key` | The secret key used for encryption/decryption |
| `grades.csv` | The original file before encryption |
| `encrypted_grades.csv` | The protected (encrypted) version of the file |
| `decrypted_grades.csv` | The restored file after decryption |

---

## How It Works

The program uses **Fernet encryption** from Python's `cryptography` library. Here's the flow in simple terms:

```
grades.csv  →  [Encrypt with key]  →  encrypted_grades.csv  (unreadable)
encrypted_grades.csv  →  [Decrypt with key]  →  decrypted_grades.csv  (restored)
```

1. A **secret key** is generated and saved to `mykey.key`
2. The key is loaded back and used to **encrypt** `grades.csv`
3. The same key is then used to **decrypt** the encrypted file
4. The decrypted output matches the original file exactly ✅

---

## How to Run

**Step 1 — Install the required library:**
```bash
pip install cryptography
```

**Step 2 — Run the script:**
```bash
python task4.py
```

That's it! The script will generate the key, encrypt the file, and decrypt it all in one go.

---

## Sample Output

When you open `encrypted_grades.csv`, it looks something like this — completely unreadable:
```
gAAAAABl3k2X9v...Xz8mNqL1w==
```

And after decryption, `decrypted_grades.csv` looks exactly like the original `grades.csv`. The data is fully restored.

---

## What I Learned

- How symmetric encryption works (same key to lock and unlock)
- How to read and write files in binary mode in Python
- The importance of keeping the key safe — lose the key, lose the data!
- Real-world use case of protecting sensitive files like student records

---

## Requirements

- Python 3.x
- `cryptography` library

---

> **Note:** Keep your `mykey.key` file safe. If it's lost, the encrypted file cannot be recovered.
