#THIS IS MY FIRST SUBMISSION, IT GOT TIMED OUT IN SOME TESTS DUE TO COMPLEXITY O(nˆk)
#!/bin/python3

import sys

iniArray = []
def manipulateArray(n,m,queries):
    iniArray[:n] = [0]*n

    for z in range(m):
        currentQuery = queries[z]
        a = currentQuery[0]
        b = currentQuery[1]
        k = currentQuery[2]
        
        for x in range((b-a)+1):
            iniArray[(a-1)+x] = iniArray[(a-1)+x] + k
        

        
    print(max(iniArray))

    
if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    queries = []
    for a0 in range(m):
        arr = list(map(int, input().strip().split(' ')))
        queries.append(arr)
    manipulateArray(n,m,queries)
