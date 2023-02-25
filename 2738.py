import sys

n, m = map(int, sys.stdin.readline().split())

arr1 = []
arr2 = []

for i in range(n):
    arr1.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    arr2.append(list(map(int, sys.stdin.readline().split())))

for i in range(len(arr1)):
    for j in range(len(arr1[i])):
        print(arr1[i][j]+arr2[i][j], end=" ")
    print()