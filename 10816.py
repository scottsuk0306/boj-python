import sys

input = sys.stdin.readline

arr1 = []
arr2 = []

n = int(input())

arr1 = list(map(int, input().split()))

m = int(input())

arr2 = list(map(int, input().split()))

dic = {}

for i in arr2:
    dic[i] = 0              # arr2안의 요소들을 dic의 key값으로 함

for i in arr1:
    if i in dic.keys():
        dic[i] += 1         # dic의 key값이 arr1에 있을 때 마다 +1

for i in arr2:              # arr2의 요소가 중복인 경우, 출력시 생략되지 않도록
    print(dic[i], end=" ")  # 출력 형식을 위와 같이 함