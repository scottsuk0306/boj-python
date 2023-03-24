import sys

input = sys.stdin.readline

def isPrime(n):                                 # 소수 판별 함수 선언
    if n == 0 or n == 1:
        return False 
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
arr = []

for i in range(2, 123456 * 2 + 1):              # 시간 절약 위해 미리 소수를 구해놓음
    if isPrime(i):
        arr.append(i)

while True:
    x = int(input())
    
    if x == 0:
        break

    cnt = 0

    for i in arr:
        if i > x and i <= 2 * x:
            cnt += 1
    print(cnt)