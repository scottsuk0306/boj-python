import sys

input = sys.stdin.readline

n = int(input())

arr= []

for _ in range(n):
    age, name = map(str, input().split())
    arr.append([int(age), name])

arr.sort(key = lambda arr : arr[0]) # lambda를 이용하여 정렬 기준을 age로 함

for i in arr:
    print(*i, end = " ")            # *i에서 *s는 출력 시 list의 형식을 없애줌
    print()