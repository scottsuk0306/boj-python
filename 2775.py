import sys 

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    floor = int(input())
    n = int(input())

    arr = [j for j in range(0, n+1)]

    for i in range(floor):
        for k in range(1, n+1):
            arr[k] += arr[k-1]

    print(arr[n])