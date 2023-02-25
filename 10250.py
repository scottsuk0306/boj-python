import sys

input = sys.stdin.readline
m = int(input())

for _ in range(m):
    h, w, n = map(int, input().split())

    if n % h == 0:
        a = h
    else:
        a = n % h
    
    if n % h == 0:
        b = n//h
    else:
        b = n//h + 1

    print(100*a+b)