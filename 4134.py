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

n = int(input())

for _ in range(n):
    x = int(input())

    while True:
        if isPrime(x) == True:
            print(x)
            break
        else:
            x += 1