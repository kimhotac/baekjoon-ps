import sys
input = sys.stdin.readline
t = int(input())
dp = [(1,0),(0,1)]
for i in range(t):
    n = int(input())
    while len(dp) <= n:
        dp.append((dp[-1][0]+dp[-2][0],dp[-1][1]+dp[-2][1]))
    print(' '.join(map(str,dp[n])))