import sys

input = sys.stdin.readline

arr = list(map(int, input().split()))

maximum = max(arr)
arr.remove(max(arr))

if maximum >= sum(arr):
    print(2 * sum(arr) - 1)             # 세 변의 합 - {가장 큰 변 길이 - (나머지 두 변의 합) + 1}
else:
    print(maximum + sum(arr))