import sys

input = sys.stdin.readline

arr = []

for i in range(5):
    x = int(input())
    arr.append(x)

arr.sort(reverse = 1)   # arr 속 요소들 크기 순 정렬

print(sum(arr)//5)      # 평균 출력
print(arr[2])           # 중앙값 출력