import sys
from math import sqrt                               # 제곱근 사용 위해 작성

input = sys.stdin.readline

repeat_time = int(input())                          # 반복 횟수

case_list = []                                      # 입력 받은 숫자들을 저장할 list

for _ in range(repeat_time):                        
    x = int(input())
    case_list.append(x)

max_num = max(case_list)                            # 입력 받은 숫자들 중 최댓값(이 값까지 소수를 구해놓기 위함)

primes = [i for i in range(max_num + 1)]            # 소수 모임
primes[0], primes[1] = False, False

for i in range(2, int(sqrt(max_num) + 1)):          # 소수 판별
    if primes[i]:
        for j in range(i * 2, max_num + 1, i):
            primes[j] = 0

for i in range(repeat_time):
    cnt = 0
    
    for j in range(2, case_list[i] // 2 + 1):
        if primes[j] and primes[case_list[i] - j]:
            cnt += 1

    print(cnt)