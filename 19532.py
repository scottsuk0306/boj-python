import sys

input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())

x = (c * e - b * f) / (a * e - b * d)
y = (c * d - a * f) / (b * d - a * e)

print("%d %d" % (x, y))