import sys

arr = list(map(int, sys.stdin.readline().split()))

idx = 0

for i in range(0, 7):
    if arr[i]+1==arr[i+1]:
        idx += 1
    elif arr[i]==arr[i+1]+1:
        idx -= 1
    else:
        pass

if idx == 7:
    print("ascending")
elif idx == -7:
    print("descending")
else:
    print("mixed")