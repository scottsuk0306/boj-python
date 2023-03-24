import sys

input = sys.stdin.readline

a, b = map(int, input().split())
    
gcd = 1                             # gcd = 최대공약수

for i in range(2, min(a, b) + 1):
    if a % i == 0 and b % i == 0:   
        gcd = i
    
lcm = a * b // gcd                  # lcm = 최소공배수
print(lcm)