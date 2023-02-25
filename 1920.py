import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

count = [0 for i in range(m)]

for i in range(n):
    for j in range(m):
        if count[j]==1:
            pass
        
        if arr[i]==check[j]:
            count[j] += 1
            break

for i in range(m):
    print(count[i])