# File: ComparingLinearBinarySearch.py
# Student: Harini Shanmugam
# UT EID: hs28663
# Course Name: CS303E
#
# Date Created: 11/5/21
# Date Last Modified: 11/5/21
# Description of Program: This program compares the performance of linear and binary search.
import math
import random


def linearSearch(lst, key):
    """ Search for key in unsorted list lst.  Note that
        the index + 1 is also the number of probes. """
    for i in range(len(lst)):
        if key == lst[i]:
            return i
    return -1


def binarySearch(lst, key):
    """ Search for key in sorted list lst. Return
        a pair containing the index (or -low - 1)
        and a count of number of probes. """
    count = 0
    low = 0
    high = len(lst) - 1
    while high >= low:
        count += 1
        mid = (low + high) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return mid, count
        else:
            low = mid + 1
    # Search failed
    return -low - 1, count


# Linear Search
num = 1
start = [i for i in range(1000)]
random.shuffle(start)
print("Linear search:")
while num < 100000:
    counter = 0
    linearTotal = 0
    for i in range(0, num):
        counter += linearSearch(start, random.randint(0, 999))
    linearTotal = float(counter/num)
    num *= 10
    print("  Tests: " + format(num, "<9d") + "Average probes: " + str(linearTotal))

# Binary Search
binaryTotal = 0
for i in range(0, 999):
    index, counter = binarySearch(start, random.randint(0, 999))
    binaryTotal += counter
difference = abs(math.log2(1000) - (binaryTotal/1000))
print("Binary search:")
print("  Average number of probes: " + str(binaryTotal/1000))
print("  Differs from log2(1000) by: " + str(difference))
