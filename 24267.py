import sys

input = sys.stdin.readline

n = int(input())

n -= 2                                      # n-2를 시그마에 대입

print((n ** 3 + 3 * n ** 2 + 2 * n) // 6)   # 시그마를 n에 관한 이차식으로 변환
print(3)