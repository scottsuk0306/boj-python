import sys

input = sys.stdin.readline

maxsize = 101
n = int(input())

arr = [[0 for i in range(maxsize)] for j in range(maxsize)]
cnt = 0

for _ in range(n):
    a, b = map(int, input().split())

    for i in range(a, a+10):
        for j in range(b, b+10):
            arr[i][j] = 1

for i in range(maxsize):
    for j in range(maxsize):
        if arr[i][j] == 1:
            cnt += 1

print(cnt)