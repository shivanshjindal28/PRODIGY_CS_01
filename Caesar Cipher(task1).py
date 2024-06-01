import getpass

def caesar_cipher_encrypt(text,shift):
    encrypted_text=""
    for char in text:
        if char.isalpha():
            shift_amount=shift%26
            new_char=chr(((ord(char.lower())-97+shift_amount)%26)+97)
            if char.isupper():
                new_char=new_char.upper()
            encrypted_text+=new_char
        else:
            encrypted_text+=char
    return encrypted_text

def caesar_cipher_decrypt(text,shift):
    return caesar_cipher_encrypt(text,-shift)

def main():
    while True:
        choice=input("Do you want to encrypt or decrypt the message? (e/d): ").lower()
        if choice not in ['e','d']:
            print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")
            continue

        message=getpass.getpass("Enter the message: ")
        
        # Show the first and last letter of the message
        if len(message)>0:
            print(f"First letter of the message: {message[0]}")
            print(f"Last letter of the message: {message[-1]}")
        else:
            print("The message is empty.")
            continue

        shift_value=getpass.getpass("Enter the shift value: ")
        
        try:
            shift=int(shift_value)
        except ValueError:
            print("Invalid shift value. Please enter an integer.")
            continue

        if choice=='e':
            encrypted_message=caesar_cipher_encrypt(message,shift)
            print(f"Encrypted message: {encrypted_message}")
        else:
            decrypted_message=caesar_cipher_decrypt(message, shift)
            print(f"Decrypted message: {decrypted_message}")

        another=input("Do you want to encrypt/decrypt another message? (y/n): ").lower()
        if another!='y':
            break

if __name__=="__main__":
    main()
