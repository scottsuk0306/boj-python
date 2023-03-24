import sys

input = sys.stdin.readline

n = int(input())

arr1 = []
arr1 = list(map(int, input().split()))

m = int(input())

arr2 = []
arr2 = list(map(int, input().split()))

dic = {}

for i in range(len(arr2)):
    dic[arr2[i]] = 0            # arr2의 key값들을 dic에 저장

for i in arr1:
    if i in dic.keys():         # arr1의 값이 dic의 key에 있다면 - 상수 시간이 소모되어 시간 복잡도를 크게 낮춤
        dic[i] += 1             # 해당하는 dic의 value값을 +1 해줌

print(*dic.values())