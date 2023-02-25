import sys

input = sys.stdin.readline

n, m = map(int, input().split())

for i in range(n, m+1):
    x = 1
    y = int(i**0.5)
    
    for j in range(2, y+1):
        if i%j==0 and i!=j:
            x = 0
            break
    
    if x == 1 and i!=1:
        print(i)