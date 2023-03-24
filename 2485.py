import sys

input = sys.stdin.readline

def gcd(a, b):                  # 최소공배수 구하는 함수
    while b > 0:                # 유클리드 호제법 이용
        a, b = b, a % b
    
    return a

n = int(input())                # 심어진 나무 총 수
a = int(input())                # 첫 번째 나무 위치

arr = []                        # 나무들 사이의 간격이 저장될 list

for i in range(n-1):
    x = int(input())
    arr.append(x - a)
    a = x

g = arr[0]

for i in range(len(arr)):
    g = gcd(g, arr[i])          # 모든 나무 간격들의 최소공배수 구하기

result = 0                      # 심어야 하는 나무 수

for i in arr:
    result += i // g - 1

print(result)