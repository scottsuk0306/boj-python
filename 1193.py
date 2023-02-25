import sys

input = sys.stdin.readline

n = int(input())

line = 0
sum = 0

while sum < n:
    line += 1
    sum += line

diff = sum - n 

if line % 2 != 1:
    print(f"{line-diff}, {1+diff}")
else:
    print(f"{1+diff}, {line-diff}")