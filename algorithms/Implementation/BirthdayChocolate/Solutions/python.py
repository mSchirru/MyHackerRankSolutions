#!/bin/python3

import sys

def solve(n, s, d, m):
    if m > n:
        return 0
    
    i = j = 0
    window_sum = 0
    
    while j < m:
        window_sum += s[j]
        j += 1
        
    count = 1 if window_sum == d else 0
    
    while j < n:
        window_sum -= s[i]
        window_sum += s[j]
        
        if window_sum == d:
            count += 1
        i += 1
        j += 1
        
    return count

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
