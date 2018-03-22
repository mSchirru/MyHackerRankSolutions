#!/bin/python3

import sys

def quickSort(arr):
    left = []
    equal = []
    right = []
    pivot = arr[0]
    for x in arr:
        if x == pivot:
            equal.append(x)
        elif x > pivot:
            right.append(x)
        else:
            left.append(x)

    arr[:] =[]
    arr += left
    arr += equal
    arr += right
    return arr


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = quickSort(arr)
    print (" ".join(map(str, result)))


