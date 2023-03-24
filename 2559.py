import sys

input = sys.stdin.readline

n, k = map(int, input().split())

arr = list(map(int, input().split()))
pfx = [0]

summ = 0

for i in arr:
    summ += i
    pfx.append(summ)                    # 누적 합 이용

max_temp = pfx[k] - pfx[0]

for i in range(n - k + 1):
    l = i
    r = i + k

    if pfx[r] - pfx[l] > max_temp:
        max_temp = pfx[r] - pfx[l]      

print(max_temp)