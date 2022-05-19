# File: RecursiveFunctions.py
# Student: Harini Shanmugam
# UT EID: hs28663
# Course Name: CS303E
#
# Date Created: 11/19/2021
# Date Last Modified: 11/19/2021
# Description of the Program: This program solves simple problems using recursion.

def sumItemsInList(L):
    """ Given a list of numbers, return the sum. """
    if L == []:
        return 0
    else:
        return L[0] + sumItemsInList(L[1:])


def countOccurrencesInList(key, L):
    """ Return the number of times key occurs in
    list L. """
    if L == []:
        return 0
    elif key == L[0]:
        return 1 + countOccurrencesInList(key, L[1:])
    else:
        return countOccurrencesInList(key, L[1:])


def addToN(n):
    """ Add up the non-negative integers to n.
    E.g., addToN( 5 ) = 0 + 1 + 2 + 3 + 4 + 5. """
    if n == 0:
        return 0
    else:
        return n + addToN(n - 1)


def findSumOfDigits(n):
    """ Return the sum of the digits in a non-negative integer. """
    if n == 0:
        return n
    else:
        return int((n % 10) + findSumOfDigits(n / 10))


def decimalToBinary(n):
    """ Given a nonnegative decimal integer n, return the
   binary representation as a string. """
    if n == 0:
        return 0
    else:
        return (n % 2) + 10 * decimalToBinary(n // 2)


def decimalToList(n):
    """ Given a nonnegative decimal integer, return a list of the
   digits (as strings). """
    if n <= 9:
        return [n]
    else:
        return decimalToList(n//10) + [n % 10]


def isPalindrome(s):
    """ Return True if string s is a palindrome and False
   otherwise. Count the empty string as a palindrome. """
    if not s:
        return True
    elif s[0] == s[-1]:
        isPalindrome(s[1:-1])
        return True
    else:
        return False


def findFirstUppercase(s):
    """ Return the first uppercase letter in
   string s, if any.  Return None if there
   is none. """
    # incomplete
    if s.isupper() is False:
        return None
    else:
        return findFirstUppercase(s[0::].isupper())


def findFirstUppercaseIndexHelper(s, index):
    """ Helper function for findFirstUppercaseIndex. """
    # incomplete


# The following function is already completed for you.  But
# make sure you understand what it's doing.

def findFirstUppercaseIndex(s):
    """ Return the index of the first uppercase letter in
   string s, if any.  Return -1 if there is none.  This one
   requires a helper function, which is the recursive
   function. """
    return findFirstUppercaseIndexHelper(s, 0)
