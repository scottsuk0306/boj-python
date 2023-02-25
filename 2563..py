import sys

n = int(sys.stdin.readline())

arr = [[0 for i in range(101)] for j in range(101)]
cnt = 0

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())

    for i in range(a, a+10):
        for j in range(b, b+10):
            arr[i][j] = 1

for i in range(101):
    for j in range(101):
        if arr[i][j]==1:
            cnt += 1

print(cnt)