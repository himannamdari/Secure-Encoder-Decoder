import base64

# Secure Encoder-Decoder using Caesar Cipher + Base64

def caesar_cipher(text, shift):
    """Applies a Caesar cipher shift to the text."""
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Keep special characters unchanged
    return result

def caesar_decipher(text, shift):
    """Reverses the Caesar cipher shift."""
    return caesar_cipher(text, -shift)

def encode(text, shift=3):
    """Encodes a string using Caesar cipher and Base64."""
    print(f"Encoding text: {text} with shift: {shift}")
    shifted_text = caesar_cipher(text, shift)
    base64_encoded = base64.b64encode(shifted_text.encode()).decode()
    print(f"Shifted text: {shifted_text}")
    print(f"Base64 Encoded: {base64_encoded}")
    return base64_encoded

def decode(encoded_text, shift=3):
    """Decodes a string by reversing Base64 and Caesar cipher."""
    print(f"Decoding text: {encoded_text} with shift: {shift}")
    base64_decoded = base64.b64decode(encoded_text.encode()).decode()
    original_text = caesar_decipher(base64_decoded, shift)
    print(f"Base64 Decoded: {base64_decoded}")
    print(f"Original text: {original_text}")
    return original_text

if __name__ == "__main__":
    original_text = "Intermediate GitHub Project!"
    shift_value = 5
    
    print("Starting encoding process...")
    encoded = encode(original_text, shift_value)
    print("Encoding complete. Starting decoding process...")
    decoded = decode(encoded, shift_value)
    print("Decoding complete.")
    
    print(f"Original: {original_text}")
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")
    
    # Save output to a file for GitHub upload
    with open("secure_output.txt", "w") as f:
        f.write(f"Original: {original_text}\n")
        f.write(f"Encoded: {encoded}\n")
        f.write(f"Decoded: {decoded}\n")
    print("Results saved successfully.")
