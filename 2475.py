import sys

arr = list(map(int, sys.stdin.readline().split()))

sum = 0

for i in range(5):
    sum += (pow(arr[i],2))

print(sum%10)