import sys 

t = int(sys.stdin.readline())

for _ in range(t):
    floor = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    arr = [j for j in range(0, n+1)]

    for i in range(floor):
        for k in range(1, n+1):
            arr[k] += arr[k-1]

    print(arr[n])