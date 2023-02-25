import sys

n = int(sys.stdin.readline())

arr = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())

check = list(map(int, sys.stdin.readline().split()))

for i in check:
    if i in arr:
        print(1)
    else:
        print(0)