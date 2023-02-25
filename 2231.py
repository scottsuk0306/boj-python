import sys

input = sys.stdin.readline

def f(n):
    sum = n
    n = list(str(n))
    size = len(n)
    
    for i in range(size):
        sum += int(n[i])
    return sum

n = int(input())

small = 1000000

for i in range(n):   
    if f(i) == n:
        small = min(small, i)

if small == 1000000:
    print(0)
else:
    print(small)