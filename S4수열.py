import sys
sys.stdin = open('input.txt', 'r')

# 0에서부터 9까지의 숫자로 이루어진 N개의 숫자가 나열된 수열
# 연속해서 커지거나(<=), 혹은 연속해서 작아지는(>=) 수열 중 가장 길이가 긴 것

n = int(input())
numbers = list(map(int,input().split()))

up_dp = [1]*n
down_dp = [1]*n

# 7
# 1 2 2 3 1 1 1

# 커지는
for i in range(n-1):
    if numbers[i] <= numbers[i+1]:
        up_dp[i+1] = up_dp[i]+1
# 작아지는
for i in range(n-1):
    if numbers[i] >= numbers[i+1]:
        down_dp[i+1] = down_dp[i]+1

print(max(up_dp+down_dp))