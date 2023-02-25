a = [0 for i in range(5)]

while True:
    a = list(map(int, str(input())))
    
    if a[0] == 0:
        break

    cnt = 0

    for i in range(len(a)//2):
        if a[i] == a[len(a)-i-1]:
            cnt += 1

    if cnt != len(a)//2:
        print("no")
    else:
        print("yes")