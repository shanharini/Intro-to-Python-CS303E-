# File: MyStringFunctions.py
# Student: Harini Shanmugam
# UT EID: hs28663
# Course Name: CS303E
#
# Date Created: 10/25/2021
# Date Last Modified: 10/25/2021
# Description of the Program: This program defines a collection of functions on strings using only ord, char, indexing,
# slicing, append (i.e., +), len, in, not in, and equality comparison (== or !=)

def myAppend( str, ch ):
    # Return a new string that is like str but with
    # character ch added at the end
    return str + ch


def myCount( str, ch ):
    # Return the number of times character ch appears
    # in str.
    count = 0
    for i in str:
        if i == ch:
            count += 1
    return count


def myExtend( str1, str2 ):
    # Return a new string that contains the elements of
    # str1 followed by the elements of str2, in the same
    # order they appear in str2.
    return str1 + str2


def myMin( str ):
    # Return the character in str with the lowest ASCII code.
    # If str is empty, print "Empty string: no min value"
    # and return None.
    if str == "":
        print("Empty string: no min value")
        return None
    else:
        minNum = 123
        for i in str:
            if ord(i) < minNum:
                minNum = ord(i)
        result = chr(minNum)
        print(result)


def myInsert( str, i, ch ):
    # Return a new string like str except that ch has been
    # inserted at the ith position.  I.e., the string is now
    # one character longer than before. Print "Invalid index" if
    # i is greater than the length of str and return None.
    if i > len(str):
        print("Invalid Index")
        return None
    else:
        return str[0:i] + ch + str[i:]


def myPop( str, i ):
    # Return two results:
    # 1. a new string that is like str but with the ith
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is greater than or
    # equal to len(str), and return str unchanged and None
    if i >= len(str):
        print("Invalid Index")
        return str, None
    else:
        return str[0:i] + str[i+1:], str[i]


def myFind( str, ch ):
    # Return the index of the first (leftmost) occurrence of
    # ch in str, if any.  Return -1 if ch does not occur in str.
    if ch not in str:
        return -1
    else:
        position = 0
        for i in str:
            if i != ch:
                position += 1
            else:
                return position


def myRFind( str, ch ):
    # Return the index of the last (rightmost) occurrence of
    # ch in str, if any.  Return -1 if ch does not occur in str.
    if ch not in str:
        return -1
    else:
        for i in range(len(str)-1, 0, -1):
            if str[i] == ch:
                return i


def myRemove( str, ch ):
    # Return a new string with the first occurrence of ch
    # removed.  If there is none, return str.
    if ch not in str:
        return str
    else:
        for i in range(0, len(str) - 1):
            if str[i] == ch:
                return str[0:i] + str[i+1:]


def myRemoveAll( str, ch ):
    # Return a new string with all occurrences of ch.
    # removed.  If there are none, return str.
    if ch not in str:
        return str
    else:
        newString = ""
        for i in str:
            if i != ch:
                newString += i
        return newString


def myReverse( str ):
    # Return a new string like str but with the characters
    # in the reverse order.
    backwards = str[::-1]
    return backwards
