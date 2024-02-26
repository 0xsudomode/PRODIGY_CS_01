#!/usr/bin/python

import argparse

def caesar_cipher(text, shift): 
    result = ""
    for char in text:
        if char.isalpha():  
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            result += chr(shifted)
        else:  
            result += char
    return result

def main():
    parser = argparse.ArgumentParser(description="Caesar Cipher Encrypter/Decrypter")
    parser.add_argument("text", help="Text to be encrypted/decrypted")
    parser.add_argument("shift", type=int, help="Shift value for encryption/decryption")
    parser.add_argument("-d", "--decrypt", action="store_true", help="Decrypt the text")
    parser.add_argument("-i", "--iterations", type=int, default=1, help="Number of iterations (default: 1)")
    args = parser.parse_args()

    if args.decrypt:
        args.shift = -args.shift  # For decryption, shift in reverse direction

    for _ in range(args.iterations):
        args.text = caesar_cipher(args.text, args.shift)

    print("Result:", args.text)

if __name__ == "__main__":
    main()
