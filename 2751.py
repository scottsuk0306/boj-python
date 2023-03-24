import sys

input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    x = int(input().strip())
    arr.append(x)

arr.sort(reverse = False) # reverse = False로 하여 arr를 오름차순으로 정렬

for i in arr:
    print(i)