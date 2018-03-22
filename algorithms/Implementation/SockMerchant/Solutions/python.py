#!/bin/python3

import sys
from collections import *
def sockMerchant(n, ar):
    numberOfPairs = 0
    c = Counter(ar)
    for k in c:
        numberOfPairs += c[k]//2
    return(numberOfPairs)
  
  
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
