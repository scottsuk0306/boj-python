import sys

input = sys.stdin.readline

n = int(input())

cnt = 0
number = 666

while True:
    a = str(number)

    for i in range(len(a) - 2):
        if a[i:i+3] == "666":
            cnt += 1
            break

    if cnt == n:
        print(number)
        break

    number += 1    