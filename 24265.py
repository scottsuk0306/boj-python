import sys

input = sys.stdin.readline

def addition(n):
    sum = 0
    
    for i in range(n):
        sum += i
    
    return sum

n = int(input())

print(addition(n)) # 1 ~ n 까지의 합 만큼 반복
print(2)