import sys

input = sys.stdin.readline

def f(n):
    if n == 0:
        return 0
    elif n == 1: 
        return 1
    else:
        return f(n-1) + f(n-2)  # 재귀함수 선언
    
n = int(input())

print(f(n))