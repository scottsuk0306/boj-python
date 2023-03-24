import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = []

for i in range(1, n+1):
    if n % i == 0:
        arr.append(i)

if len(arr) < m:
    print(0)
else:
    print(arr[m-1])