import sys

n = int(sys.stdin.readline())

x = 10000
y = 10000
sum = x+y

for i in range((n//3)+1):
    if (n-3*i)%5==0:
        x = (n-3*i)//5
        y = i
    
    if sum>x+y:
        sum = x+y

if x+y==20000:
    print("-1")
else:
    print(sum)