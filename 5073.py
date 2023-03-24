import sys

input = sys.stdin.readline

def isTriangle(arr):
    maximum = max(arr)
    arr.remove(maximum)

    if maximum >= sum(arr):
        arr.append(maximum)                 # remove했던 maximum값을 다시 append해주어야 함
        return False
    
    arr.append(maximum)
    return True


while True:
    arr = list(map(int, input().split()))

    if arr[0] == arr[1] == arr[2] == 0:
        break

    if isTriangle(arr) is False:
        print("Invalid")
    else: 
        if len(set(arr)) == 1:              # set된 arr의 len을 이용하여 변끼리의 상관관계를 구함
            print("Equilateral")
        elif len(set(arr)) == 2:
            print("Isosceles")
        else: 
            print("Scalene")  