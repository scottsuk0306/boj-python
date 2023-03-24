import sys

input = sys.stdin.readline

def recursion(s, l, r):
    if l >= r:
        return 1, l+1                   # 재귀횟수 -1인 l에 +1 한 값을 return 하도록
    elif s[l] != s[r]:
        return 0, l+1                   # 마찬가지
    else:
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

n = int(input())

for i in range(n):
    x = list(map(str, input().strip()))
    print(*isPalindrome(x))