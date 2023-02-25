import sys

x, y, w, h = map(int, sys.stdin.readline().split())

arr = [x, y, w-x, h-y]

min = arr[0]

for i in range(1, 4):
    if arr[i]<min:
        min = arr[i]

print(min)