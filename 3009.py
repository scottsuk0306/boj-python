import sys

input = sys.stdin.readline

arr_x = []
arr_y = []
answer = []

for _ in range(3):
    x, y = map(int, input().split())
    arr_x.append(x)
    arr_y.append(y)

if arr_x[0] == arr_x[1]:            # x좌표 찾는 과정
    answer.append(arr_x[2])
elif arr_x[1] == arr_x[2]:
    answer.append(arr_x[0])
else:
    answer.append(arr_x[1])

if arr_y[0] == arr_y[1]:            # y좌표 찾는 과정
    answer.append(arr_y[2])
elif arr_y[1] == arr_y[2]:
    answer.append(arr_y[0])
else:
    answer.append(arr_y[1])

print(*answer)