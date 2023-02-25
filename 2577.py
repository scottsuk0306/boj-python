import sys

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
count = [0 for _ in range(10)]
arr = [0 for _ in range(3)]
multiple = 1

for i in range(3):
    arr[i] = int(sys.stdin.readline())
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