import sys

input = sys.stdin.readline

n = int(input())

sum = 1
cnt = 1

if n == 1: 
    cnt = 1
else:
    while True:
        sum += 6 * cnt
        cnt += 1
        if n <= sum:
            break
        else:
            continue

print(cnt)        