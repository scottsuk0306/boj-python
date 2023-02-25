import sys

def f(n):
    sum = n
    n = list(str(n))
    size = len(n)
    
    for i in range(size):
        sum += int(n[i])
    return sum

n = int(sys.stdin.readline())

idx = 1000000000

for i in range(n):   
    if f(i)==n:
        if idx>=i:
            idx = i

if idx == 1000000000:
    print(0)
else:
    print(idx)