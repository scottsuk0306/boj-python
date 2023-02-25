a, b = (15, 5)

arr=[[-1 for i in range(a)] for j in range(b)]

for i in range(b):
    d = list(input())

    for j in range(len(d)):
        arr[i][j] = d[j]

for i in range(a):
    for j in range(b):
        if arr[j][i] == -1:
            continue
        else:
            print(arr[j][i], end="")