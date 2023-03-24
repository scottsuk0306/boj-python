import sys

input = sys.stdin.readline

def func(n, m):
    if n == 0 and m == 0:
        return 0
    elif m % n == 0:
        print("factor")
    elif n % m == 0:
        print("multiple")
    else:
        print("neither")

while True:
    x, y = map(int, input().split())
    func(x, y)
    
    if x == 0 and y == 0:
        break