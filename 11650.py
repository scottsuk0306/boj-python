import sys

input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    x, y = map(int, input().split())
    arr.append([x, y])

arr.sort(key = lambda arr : (arr[0], arr[1])) # lambda를 이용하여 x 기준(arr[0]) 오름차순 정렬 + x 동일 시 y 기준(arr[1])으로 오름차순 정렬

for x, y in arr:
    print("%d %d" %(x, y))