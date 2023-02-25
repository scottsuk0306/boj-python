import sys

n = int(sys.stdin.readline())

line = 0
sum = 0

while sum<n:
    line += 1
    sum += line

diff = sum - n 

if line%2!=1:
    print("%d/%d" % (line-diff, 1+diff))
else:
    print("%d/%d" % (1+diff, line-diff))