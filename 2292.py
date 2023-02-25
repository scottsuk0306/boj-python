import sys

n = int(sys.stdin.readline())

sum = 1
cnt = 1

if n==1: 
    cnt = 1
else:
    while True:
        sum += cnt+1 + cnt*4 + cnt-1
        cnt += 1
        if n<=sum:
            break
        else:
            continue

print(cnt)        