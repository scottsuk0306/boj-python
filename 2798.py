import sys
import itertools
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))

sum_list = [sum(i) for i in itertools.combinations(arr, 3) if sum(i) <= m]

print(max(sum_list))