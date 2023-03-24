import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
num_remains = [0 for i in range(m)]     # 각 나머지에 해당하는 누적 합의 경우의 수들을 요소로 가진 list

summ = 0

for i in arr:
    summ += i
    num_remains[summ % m] += 1          # 각 나머지가 나오는 경우에 +1

result = num_remains[0]                 # 2가지 선택 필요 X(그 자체만으로 조건 충족 가능)

for i in num_remains:                   
    result += i * (i - 1) // 2          # 조합과 같은 개념(i가지 경우에서 임의로 2가지를 뽑는 경우의 수)

print(result)