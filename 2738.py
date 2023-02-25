import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr1 = []
arr2 = []

for i in range(n):
    arr1.append(list(map(int, input().split())))

for i in range(n):
    arr2.append(list(map(int, input().split())))

for i in range(len(arr1)):
    for j in range(len(arr1[i])):
        print(arr1[i][j]+arr2[i][j], end=" ")
    print()