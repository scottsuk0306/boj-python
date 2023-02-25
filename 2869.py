import sys

input = sys.stdin.readline

a, b, v = map(int, input().split())

sum = v - a
cnt = 1

cnt += sum // (a-b)

if sum % (a-b) != 0: 
    cnt += 1

print(cnt)