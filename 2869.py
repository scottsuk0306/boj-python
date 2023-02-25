import sys

a, b, v = map(int, sys.stdin.readline().split())

sum = v - a
cnt = 1

cnt += sum // (a-b)

if sum % (a-b) != 0: 
    cnt += 1

print(cnt)