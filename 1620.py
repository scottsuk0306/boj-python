import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dic = {input().strip(): i for i in range(1, n+1)}   # 시간 복잡도를 줄이기 위해 dictionary 사용
reverse_dic = dict(map(reversed, dic.items()))      # 숫자로 입력되는 경우를 위해 reverse된 새로운 
                                                    # dictionary도 선언
for i in range(m):
    x = input().strip()

    if x in dic.keys():                             # input 값이 dic의 key값과 같은 경우
        print(dic[x])
    else:                                           # input 값이 dic의 value값과 같은 경우
        print(reverse_dic[int(x)])                  # input 값이 str로 입력 된 정수이므로 int로 변환