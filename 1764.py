import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr1 = set(input() for i in range(n))   # 중복 제거하며 input받음
arr2 = set(input() for i in range(m))   # 중복 제거하며 input받음

answer = list(arr1 & arr2)              # answer는 arr1, arr2의 공통된 요소가 담긴 list
answer.sort()

print(len(answer))

for i in answer:
    print(i.strip())