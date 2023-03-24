import sys

input = sys.stdin.readline

a = input()

arr = []

for i in range(len(a)):
    arr.append(a[i])

arr.sort(reverse = True)    # arr 속 요소들을 내림차순으로 정렬

for i in range(len(arr)):
    print(arr[i], end="")