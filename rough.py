lst1=list(range(1,27))
lsta=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
d1a=dict(zip(lst1,lsta ))
print(d1a)
da1={value:key for key,value in d1a.items()}
print(da1)
d2a={i:i*i for i in lst1}
print(d2a)

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