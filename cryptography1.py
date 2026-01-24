def encrypt(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            result += char  # keep spaces and symbols
    
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


# Example
msg = "HELLO WORLD"
encrypted = encrypt(msg, 3)
decrypted = decrypt(encrypted, 3)

print("Original:", msg)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)