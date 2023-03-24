import sys

input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    x = str(input().strip()) # strip 함수를 통해 x에 순수 문자열만 저장
    arr.append([x, len(x)])

arr.sort(key = lambda arr : (arr[1], arr[0])) # len을 기준으로 우선 정렬되게 함, len 동일 시 사전식 정렬
removed = []

for i, j in arr:
    if i not in removed:
        removed.append(i) # arr에서 중복제거하여 removed에 append함

for i in removed:
    print(i, end=" ")
    print()