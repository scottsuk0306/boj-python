import sys

input = sys.stdin.readline

n = int(input())

arr_x = []
arr_y = []

for i in range(n):
    x, y = map(int, input().split())
    arr_x.append(x)
    arr_y.append(y)

max_x, min_x = max(arr_x), min(arr_x)   # 밑변 좌표 구하기
max_y, min_y = max(arr_y), min(arr_y)   # 높이 좌표 구하기

hor = max_x - min_x                     # 직사각형의 밑변 길이
ver = max_y - min_y                     # 직사각형의 높이 길이

print(hor * ver)