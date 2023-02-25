import sys

input = sys.stdin.readline

n = int(input())

flag = False

for i in range((n//3)+1):
    if (n-3*i) % 5 == 0:
        x = (n-3*i)//5
        y = i
        flag = True
        break

if not flag:
    print("-1")
else:
    print(x+y)