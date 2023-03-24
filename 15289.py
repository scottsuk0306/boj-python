import sys

input = sys.stdin.readline

n = int(input())

arr = input()
h = 0
r = 31
m = 1234567891

for i in range(n):
    h += (ord(arr[i]) - 96) * (r ** i)

print(h % m)