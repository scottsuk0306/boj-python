import sys

input = sys.stdin.readline

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if a1 * n0 + a0 <= c * n0 and a1 <= c: # 값 비교 + 기울기 비교(n >= n0인 모든 n에서 성립하기 위하여)
    print(1)
else:
    print(0)