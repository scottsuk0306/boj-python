import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

new_arr = list(set(arr))                            # 중복 제거한 arr를 새로운 list인 new_arr에 저장
new_arr.sort(reverse = False)

dic = {new_arr[i] : i for i in range(len(new_arr))} # 시간복잡도를 줄이기 위하여 dictionary 사용
    
for i in arr:
    print(dic[i], end=" ")