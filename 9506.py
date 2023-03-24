import sys

input = sys.stdin.readline

def func(n):
    arr = ["="]
    sum = 0

    for i in range(1, n):
        if n % i == 0:
            arr.append(i)
            arr.append("+")
    
    del arr[-1] # del 함수를 이용하여 arr의 마지막 요소 제거

    for i in arr:
        if type(i) == int:
            sum += i
    
    if sum == n:
        print(n, *arr)

    else:
        print(f"{n} is NOT perfect.")

while True:
    x = int(input())
    
    if x == -1:
        break
    
    func(x)