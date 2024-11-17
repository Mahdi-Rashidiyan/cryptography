def caesar_cipher(text, shift):
    result = ""

    # Traverse through each character in the text
    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # Non-alphabetic characters are added unchanged

    return result

if __name__ == "__main__":
    plaintext = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value (integer): "))
    encrypted_text = caesar_cipher(plaintext, shift)
    print(f"Encrypted text: {encrypted_text}")