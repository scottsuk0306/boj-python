import sys

input = sys.stdin.readline

n = int(input())

arr = []

for i in range(n):
    age, name = map(str, input().split())
    arr.append([int(age), i, name]) # 입력 받은 순서대로 뽑기 위해 i도 arr에 붙임

arr.sort()

for i in range(n):
    print(arr[i][0], arr[i][2])