import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))
pfs = [0]                                   # pfs list에 미리 0을 추가하여 line 20에서 혼동 방지                       
answer = []                         

summ = 0

for i in arr:
    summ += i
    pfs.append(summ)                        # 누적합(prefix sum)

for _ in range(m):
    x, y = map(int, input().split())

    answer.append(pfs[y] - pfs[x - 1])

for i in answer:
    print(i)