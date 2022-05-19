# File: Project2.py
# Student: Harini Shanmugam
# UT EID: hs28663
# Course Name: CS303E
#
# Date Created: 11/8/21
# Date Last Modified: 11/8/21
# Description of Program: This program encrypts or decrypts input from the user.

import random

# A global constant defining the alphabet.
LCLETTERS = "abcdefghijklmnopqrstuvwxyz"


def isLegalKey(key):
    # A key is legal if it has length 26 and contains all letters.
    # from LCLETTERS.
    return len(key) == 26 and all([ch in key for ch in LCLETTERS])


def makeRandomKey():
    # A legal random key is a permutation of LCLETTERS.
    lst = list(LCLETTERS)  # Turn string into list of letters
    random.shuffle(lst)  # Shuffle the list randomly
    return ''.join(lst)  # Assemble them back into a string


class SubstitutionCipher:
    def __init__(self, key=makeRandomKey()):
        if isLegalKey(key):
            self.__key = key
        else:
            print("Key entered is not legal")

    def getKey(self):
        return self.__key

    def setKey(self, newKey):
        self.__key = isLegalKey(newKey)

    def encryptText(self, plaintext):
        return plaintext

    def decryptText(self, ciphertext):
        return ciphertext


def main():
    cipher = SubstitutionCipher()
    user = input("Enter a command(getKey, changeKey, encrypt, decrypt, quit): ")
    userLowered = user.lower()

    while userLowered != "quit":
        if userLowered == "getkey":
            print("  Current cipher key: " + cipher.getKey())




        elif userLowered == "changekey":
            changeKeyInput = input("  Enter a valid cipher key, 'random' for a random key, or 'quit' to quit: ")
            if changeKeyInput == "random":
                # need to store random key as new getkey
                print("    New cipher key: " + makeRandomKey())
            elif isLegalKey(changeKeyInput):
                print("    New cipher key: " + changeKeyInput)
            elif changeKeyInput == "quit":
                break
            else:
                print("    Illegal key entered. Try again!")





        elif userLowered == "encrypt":
            encryptInput = input("  Enter a text to encrypt: ")
            print("    The encrypted text is: " + cipher.encryptText(encryptInput))

        elif userLowered == "decrypt":
            decryptInput = input("  Enter a text to decrypt: ")
            print("    The decrypted text is: " + cipher.decryptText(decryptInput))

        else:
            print("  Command not recognized. Try again!")

        user = input("Enter a command(getKey, changeKey, encrypt, decrypt, quit): ")
        userLowered = user.lower()

    if userLowered == "quit":
        print("Thanks for visiting!")


main()
