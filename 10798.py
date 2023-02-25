arr=[[-1 for i in range(15)] for j in range(5)]

for i in range(5):
    d = list(input())

    for j in range(len(d)):
        arr[i][j] = d[j]

for i in range(15):
    for j in range(5):
        if arr[j][i]==-1:
            continue
        else:
            print(arr[j][i], end="")