import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

answer = list(set(arr1) ^ set(arr2))    # arr1, arr2의 대칭차집합 구하기

print(len(answer))