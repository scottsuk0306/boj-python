import sys

input = sys.stdin.readline

n = int(input())
sum_arr = 0

arr = list(map(int, input().split()))
arr.sort(reverse = False)               # arr를 오름차순으로 정렬

for i in range(len(arr)):
    sum_arr += arr[i] * (len(arr) - i)

print(sum_arr)