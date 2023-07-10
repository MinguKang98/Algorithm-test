# 2293_동전1_Gold5
# https://www.acmicpc.net/problem/2293


n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))


def solution1():
    dp = [[0 for _ in range(k + 1)] for _ in range(n)]
    for i in range(n):
        for j in range(1, k + 1):
            if i == 0 and j % coins[i] == 0:
                dp[i][j] = 1
                continue
            if coins[i] > j:
                dp[i][j] = dp[i - 1][j]
            elif coins[i] == j:
                dp[i][j] = dp[i - 1][j] + 1
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i]]

    return dp[-1][-1]


"""
dp 를 사용
dp[i][j] 는 coins[i] 까지 사용하여 j 를 만들 수 있는 경우의 수, 즉 특정 동전을 사용해 합이 i원이 되는 경우의 수
coins[i] 가 j 보다 작으면 dp[i][j] = dp[i-1][j]
coins[i] 가 j 와 같으면 dp[i][j] = dp[i-1][j] + 1
coins[i] 가 j 보다 크면 dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]

=> 메모리 초과
"""


def solution2():
    dp = [0 for _ in range(k + 1)]
    for i in range(n):
        for j in range(1, k + 1):
            if i == 0 and j % coins[i] == 0:
                dp[j] = 1
                continue
            if coins[i] > j:
                continue
            elif coins[i] == j:
                dp[j] += 1
            else:
                dp[j] += dp[j - coins[i]]

    return dp[-1]


"""
이차원이 아닌 일차원 배열로 풀어야 메모리 초과 안날듯
=> 성공
"""


def solution3():
    dp = [0 for _ in range(k + 1)]
    dp[0] = 1

    for coin in coins:
        for i in range(coin, k + 1):
            if coin <= i:
                dp[i] += dp[i - coin]

    return dp[-1]


"""
dp[0]=1 로 설정하는 이유는 solultion2 에서 coins[i] == j 일때 dp[j] += 1 하는 거 처럼
coin == i 일 때 1을 더해주기 위해서이다.
"""

print(solution3())
