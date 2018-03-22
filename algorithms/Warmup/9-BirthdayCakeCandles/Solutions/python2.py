# SOLUÇAO SEM USAR FUNÇOES DO PYTHON

import sys

def birthdayCakeCandles(n, ar):
    maxCandle = ar[0]
    count = 0
    for candle in range(n):
        if ar[candle] > maxCandle:
            maxCandle = ar[candle]
            
    for candle in ar:
        if candle == maxCandle:
            count += 1
            
        
    return count
        
        

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
