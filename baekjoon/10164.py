import sys

n, m, k = map(int, sys.stdin.readline().split())

dp = [[1]*m for _ in range(n)]

if k == 0:
    for i in range(n):
        for j in range(m):
            if i == 0:
                dp[i][j] = 1
            elif j ==0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

else:
    target_x = (k-1) // m
    target_y = (k-1) % m

    for i in range(target_x + 1):
        for j in range(target_y + 1):
            if i == 0:
                dp[i][j] = 1
            elif j ==0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    for i in range(target_x, n):
        for j in range(target_y, m):
            if target_x == i and target_y == j:
                continue
            if i == 0:
                dp[i][j] = 1
            elif j ==0:
                dp[i][j] = 1
            else:
                if target_x >= i:
                    dp[i][j] = dp[i][j-1]
                elif target_y >= j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[n-1][m-1])
