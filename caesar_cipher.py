def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift  # Reverse the shift for decryption

    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97  # Handle uppercase and lowercase letters separately
            # Shift character and wrap around using modulo 26
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Leave non-alphabetical characters unchanged

    return result


def main():
    print("Caesar Cipher Encryption/Decryption")
    mode = input("Would you like to encrypt or decrypt? (enter 'encrypt' or 'decrypt'): ").lower()
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    # Perform the cipher operation
    result = caesar_cipher(message, shift, mode)

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
