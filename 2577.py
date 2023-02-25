import sys

input = sys.stdin.readline

number = [str(i) for i in range(10)]
count = [0 for _ in range(10)]
arr = [0 for _ in range(3)]
multiple = 1

for i in range(3):
    arr[i] = int(input())
    multiple *= arr[i]

size = len(str(multiple))
multiple = str(multiple)

cnt = 0

for i in range(len(multiple)):
    for j in range(10):
        if multiple[i] == number[j]:
            count[j] += 1

for i in range(10):
    print(count[i])