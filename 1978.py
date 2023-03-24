import sys

def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

cnt = 0

for i in range(n):
    if isPrime(arr[i]):
        cnt += isPrime(arr[i])

print(cnt)