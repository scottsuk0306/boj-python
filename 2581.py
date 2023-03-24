import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

cnt = 1
sum = 0
minimum = 0

for i in range(m):       # 소수 판별 알고리즘 사용
    if cnt ** 2 >= m:
        break
    
    cnt += 1

arr = [i for i in range(m+1)]
arr[1] = 0

for i in range(n, m+1):
    for j in range(2, cnt+1):
        if arr[i] % j == 0 and arr[i] != j:
            arr[i] = 0
            break

for i in range(n, m+1):
    if arr[i] != 0:
        minimum = arr[i]
        break

for i in range(n, m+1):
    sum += arr[i]

if sum == 0:
    print(-1)

else:
    print(sum)
    print(minimum)