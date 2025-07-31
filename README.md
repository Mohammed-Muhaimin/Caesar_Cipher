
# PRODIGY_CS_01

# Caesar Cipher 🔐

## Description 📝
This is a simple Python implementation of the **Caesar Cipher** encryption and decryption technique. The Caesar Cipher works by shifting letters in the alphabet by a fixed amount. It can be used to encode or decode a message by specifying the direction (encrypt or decrypt).

## How It Works ⚙️
1. The user is prompted to **choose** whether they want to `encode` (encrypt) or `decode` (decrypt) a message.
2. The user enters their message, which is converted to lowercase for consistency.
3. The user specifies a **shift value**, determining how many positions each letter moves in the alphabet.
4. The program then processes the message:
   - If encoding, each letter is shifted **forward**.
   - If decoding, each letter is shifted **backward**.
5. Non-alphabet characters (such as numbers, spaces, and punctuation) remain unchanged.
6. The encrypted or decrypted result is displayed.
7. The user can choose to **run again** or exit the program.

## Example Usage 🎯
```plaintext
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello
Type the shift number:
3
Here is the encoded result: khoor
```

```plaintext
Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
khoor
Type the shift number:
3
Here is the decoded result: hello
```

## Features 🚀
✅ Simple and beginner-friendly Python implementation.
✅ Works with **both encryption and decryption**.
✅ Handles non-alphabet characters properly.
✅ Allows users to continue or exit as needed.

## How to Run ▶️
1. Copy the Python code into a file (e.g., `caesar_cipher.py`).
2. Run the script in a Python environment:
   ```bash
   python caesar_cipher.py
   ```
3. Follow the prompts to **encrypt or decrypt** messages.

## Thank You! 🎉
We hope you enjoy using this simple Caesar Cipher program! Have fun encrypting and decrypting messages! 🔏

