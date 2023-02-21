a = [1, 1, 2, 2, 2, 8]
print(sum(a))
b = list(map(int, input().split()))

for i in range (0,6):
    print(sum(a[i], -b[i]), end=" ")
    