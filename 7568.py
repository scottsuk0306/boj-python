import sys

input = sys.stdin.readline

n = int(input())

weight = []
height = []
degree = []

for _ in range(n):
    x, y = map(int, input().split())
    weight.append(x)
    height.append(y)

for i in range(n):
    cnt = 1

    for j in range(n):
        if weight[i] < weight[j] and height[i] < height[j]: 
            cnt += 1 # 그냥 자기보다 키, 몸무게 모두 큰 사람 있는 경우, 등수 +1
    
    degree.append(cnt)

for i in degree:
    print(i, end = " ")