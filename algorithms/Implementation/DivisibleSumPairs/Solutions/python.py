#!/bin/python3

import sys

def divisibleSumPairs(n, k, ar):
    count = 0
    arrPairs = []
  
    for x in range(len(ar)):
        j = 1
        while j < len(ar):
            pair = []
            if x < j and ((ar[x] + ar[j]) % k == 0):
                pair.append(x)
                pair.append(j)
                if pair not in arrPairs:
                    arrPairs.append(pair)
                    count += 1
            j += 1
    return count


n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs( n, k, ar)
print(result)
