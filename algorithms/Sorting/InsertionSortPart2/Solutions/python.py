#!/bin/python3

import sys

def insertionSort2(n, l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
            l[j+1],l[j] = l[j],l[j+1]
            j -= 1
        l[j+1] = key
        print(" ".join(map(str,l)))  
    

    

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    insertionSort2(n, arr)
