import sys

input = sys.stdin.readline

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1) # 재귀
    
n = int(input())

print(factorial(n))