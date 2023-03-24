import sys

input = sys.stdin.readline

from collections import Counter    # 최빈값 구하는 함수에 필요한 collections 모듈의 counter class

def modefinder(numbers):           # 최빈값 구하는 함수
    data_dic = Counter(numbers)
    order = data_dic.most_common()
    maximum = order[0][1]

    mode_list = []
    
    for num in order:
        if num[1] == maximum:
            mode_list.append(num[0])
    return mode_list

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort()                          # arr를 내림차순 정리

sum = 0

for i in range(n):
    sum += arr[i]       

print("%.f" % round(sum/n))         # round function 사사오입 규칙 주의
print(arr[n//2])                    # 중앙값
if len(modefinder(arr)) > 1:        # 최빈값
    print(modefinder(arr)[1]) 
else:
    print(modefinder(arr)[0])
print(arr[n-1]-arr[0])              # 범위