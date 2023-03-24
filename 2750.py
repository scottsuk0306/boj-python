import sys

input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    x = int(input())
    arr.append(x)

arr.sort(reverse = 0)   # 내림차순 정렬

for i in arr:
    print(i)