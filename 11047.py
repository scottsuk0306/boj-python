import sys

n, m = map(int, input().split())
cnt = 0

arr = []

for i in range(n):
    arr.append(int(input()))

arr.sort(reverse = True)        # 큰 수부터 반복문 수행하기 위해 arr를 내림차순으로 정렬

for i in arr:
    if m >= i:
        cnt += m // i
        m = m % i

        if m == 0:
            break

print(cnt)