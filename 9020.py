import sys

input = sys.stdin.readline

def isPrime(n):                             # 소수 판별 함수 선언
    if n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True

n = int(input())

for _ in range(n):
    x = int(input())

    for i in range(x//2, x + 1):            # i를 x//2부터 시작하여, 결과의 차가 가장 적은 것이 가장 먼저 출력되도록 함
        if isPrime(i) and isPrime(x - i):   
            print("%d %d" % (x-i, i))
            break