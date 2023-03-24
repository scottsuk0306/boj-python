import sys

input = sys.stdin.readline

n, m = map(int, input().split())

s = []

for i in range(n):
    x = str(input().strip())
    s.append(x)

arr = []

for i in range(m):
    y = str(input().strip())
    arr.append(y)

cnt = 0

for i in arr:           # for문을 사용하여 확인
    if i in s:
        cnt += 1

print(cnt)