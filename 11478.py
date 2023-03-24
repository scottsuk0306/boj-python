import sys

input = sys.stdin.readline

s = input().strip()             # 개행문자 제거 위해 strip() 함수 사용
arr = []

for i in range(len(s)):
    for j in range(i, len(s)):
        temp = s[i : j+1]       # 가능한 경우들
        arr.append(temp)

arr = set(arr)                  # 중복 제거
print(len(arr))