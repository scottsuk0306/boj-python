import sys

input =sys.stdin.readline

arr = []

for i in range(3):
    arr.append(int(input()))

if len(set(arr)) == 1:                          # set 함수를 이용하여 중복되는 수의 개수를 찾음
    print("Equilateral")
elif sum(arr) == 180 and len(set(arr)) == 2:
    print("Isosceles")
elif sum(arr) == 180 and len(set(arr)) == 3:
    print("Scalene")
else:
    print("Error")