def substitution_cipher(text, substitution_dict):
    result = ""

    # Traverse through each character in the text
    for char in text:
        if char.isalpha():
            # Preserve case
            if char.isupper():
                result += substitution_dict[char.lower()].upper()
            else:
                result += substitution_dict[char]
        else:
            result += char  # Non-alphabetic characters are added unchanged

    return result

# Example usage
if __name__ == "__main__":
    plaintext = "Hello, World!"
    # Example substitution dictionary
    substitution_dict = {
        'a': 'q', 'b': 'w', 'c': 'e', 'd': 'r', 'e': 't',
        'f': 'y', 'g': 'u', 'h': 'i', 'i': 'o', 'j': 'p',
        'k': 'a', 'l': 's', 'm': 'd', 'n': 'f', 'o': 'g',
        'p': 'h', 'q': 'j', 'r': 'k', 's': 'l', 't': 'z',
        'u': 'x', 'v': 'c', 'w': 'v', 'x': 'b', 'y': 'n',
        'z': 'm'
    }
    encrypted_text = substitution_cipher(plaintext, substitution_dict)
    print(f"Plaintext: {plaintext}")
    print(f"Encrypted: {encrypted_text}")