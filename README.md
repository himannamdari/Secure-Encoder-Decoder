# Secure Encoder-Decoder

## 🔐 About the Project
This Python project combines **Caesar Cipher** and **Base64 encoding** to securely encode and decode messages. It’s a simple way to explore basic encryption techniques while having fun with secret messages!

## 🚀 Features
- Encrypt messages using Caesar Cipher shifts.
- Add an extra security layer with Base64 encoding.
- Easily decode messages back to their original form.
- Customizable shift values for different encryption levels.

## 🛠️ How It Works
### Encoding Process
1. Apply a **Caesar Cipher shift** to the input text.
2. Convert the shifted text into **Base64 encoding**.
3. Output the encoded message.

### Decoding Process
1. Reverse the **Base64 encoding**.
2. Apply the inverse **Caesar Cipher shift**.
3. Retrieve the original message.

## 💻 Getting Started
### Prerequisites
Make sure you have **Python 3** installed on your system.

### Running the Script
```bash
python secure_encoder_decoder.py
```

### Example Usage
```
Original: Secret GitHub Message!
Encoded: U2VjcmV0IEdpdEh1YiBNZXNzYWdlIQ==
Decoded: Secret GitHub Message!
```

## 🤝 Contributing
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Make your improvements.
4. Submit a Pull Request.

## 📜 License
This project is licensed under the **MIT License**. Feel free to modify and use it!
