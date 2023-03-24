import sys

input = sys.stdin.readline

n = int(input())

m = 2               # 가장 작은 소수부터 시작

while n != 1:       
    if n % m == 0:  
        n //= m     
        print(m)    
    
    else:
        m += 1