import sys

n = int(sys.stdin.readline())

for _ in range(n):
    h, w, n = map(int, sys.stdin.readline().split())

    if n%h==0:
        a = h
    else:
        a = n%h
    
    if n%h==0:
        b = n//h
    else:
        b = n//h + 1

    print(100*a+b)