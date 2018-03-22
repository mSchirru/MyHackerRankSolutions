#!/bin/python3

import sys
from collections import *

def migratoryBirds(n, ar):
    c = Counter(ar).most_common(1)
    return (c[0][0])

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
