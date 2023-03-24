import sys

input = sys.stdin.readline

a, b = map(int, input().split())

if a > b:
    a, b = b, a

sum_ab = b * (b + 1) // 2 - a * (a - 1) // 2    # 시그마 공식 사용

print(sum_ab)