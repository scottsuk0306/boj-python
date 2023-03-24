import sys

input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b = b, a % b             # 유클리드 호제법
    
    return a

x, a = map(int, input().split())
y, b = map(int, input().split())

lower = a * b                       # 약분 전 분모
upper = x * b + y * a               # 약분 전 분자

gcd = gcd(lower, upper)
print(upper // gcd, lower // gcd)