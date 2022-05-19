# File: FindPrimeFactors.py
# Student: Harini Shanmugam
# UT EID: hs28663
# Course Name: CS303E
#
# Date Created: 10/29/2021
# Date Last Modified: 10/29/2021
# Description of the Program: This program accepts an integer from the user and outputs its prime factorization
import math

print("Find Prime Factors:")
user = int(input("Enter a positive integer (or 0 to stop): "))
listOfPrimes = []


def isPrime(num):
    if num < 2 or num % 2 == 0:
        return num == 2
    divisor = 3
    while divisor <= math.sqrt(num):
        if num % divisor == 0:
            return False
        else:
            divisor += 2
    return True


def findNextPrime(num):
    if num < 2:
        return 2
    if num % 2 == 0:
        num -= 1
    guess = num + 2
    while not isPrime(guess):
        guess += 2
    return guess


def primeFactorization(num):
    listOfPrimes = []
    d = 2
    while num > 1:
        if num % d == 0:
            listOfPrimes.append(d)
            num = num / d
        else:
            d = findNextPrime(d)
    return listOfPrimes


while user != 0:
    if user == 1:
        print("  1 has no prime factorization.")
    elif user < 0:
        print("  Negative integer entered. Try again.")
    elif isPrime(user):
        listOfPrimes.append(user)
        print("  The prime factorization of", user, "is:", listOfPrimes)
    else:
        print("  The prime factorization of", user, "is:", primeFactorization(user))

    print("")
    user = int(input("Enter a positive integer (or 0 to stop): "))

if user == 0:
    print("Goodbye!")
