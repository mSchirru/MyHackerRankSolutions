#!/bin/python3

import sys

def insertionSort1(n, arr):
    last = arr[-1]
    last = arr[-1]
    x = 0
    while arr[n-(n+2) - x] > last:
        arr[-1-x] = arr[n-(n+2) - x]
        print (' '.join(str(y) for y in arr))
        if x+2 == len(arr):
            arr[n-(n+2) - x] = last
            break
        else:
            x += 1
            
    if arr[n-(n+2) - x] < last:
        arr[-x-1] = last
        print (' '.join(str(y) for y in arr))
    else:
        print (' '.join(str(y) for y in arr))

 


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    insertionSort1(n, arr)
