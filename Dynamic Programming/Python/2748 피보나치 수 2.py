n = int(input())
dp = [0 for i in range(91)]

dp[1] = 1
dp[2] = 1

for i in range(3, n+1) :
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])


# https://www.acmicpc.net/source/share/039ba33d85624c519719fb11cabb6406
