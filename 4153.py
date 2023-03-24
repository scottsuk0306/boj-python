import sys

input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
        break

    big = max(a, b, c)

    if big ** 2 == a ** 2 + b ** 2 or big ** 2 == b ** 2 + c ** 2 or big ** 2 == c ** 2 + a ** 2:
        print("right")
    else:
        print("wrong")