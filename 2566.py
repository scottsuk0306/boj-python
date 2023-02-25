import sys

input = sys.stdin.readline

arr = []

for i in range(9):
    arr.append(list(map(int, input().split())))

max = arr[0][0]
x = 0
y = 0

for i in range(9):
    for j in range(9):
        if max<arr[i][j]:
            max = arr[i][j]
            x = i
            y = j

print(max)
print(f"{x+1} {y+1}")