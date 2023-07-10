# 2294_동전2_Gold5
# https://www.acmicpc.net/problem/2294
import sys

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))


def solution0():
    dp = [0 for _ in range(k + 1)]
    for i in range(n):
        for j in range(1, k + 1):
            if i == 0 and j % coins[i] == 0:
                dp[j] = j // coins[i]
                continue

            if coins[i] > j:
                continue
            elif coins[i] == j:
                dp[j] = 1
            else:
                if not dp[j - coins[i]]:  # 만들 수 없는 경우
                    dp[j] = 0
                else:
                    if dp[j] > 0:
                        dp[j] = min(dp[j], 1 + dp[j - coins[i]])
                    else:
                        dp[j] = 1 + dp[j - coins[i]]

    if not dp[-1]:
        return -1
    return dp[-1]


"""
dp[j] 안에 들어가야 하는 것은 합이 j 가 되는 동전의 최소 개수 
coins[i] == j 라면 현재 코인 하나로 만들 수 있으므로 dp[j] = 1
coins[i] < j 라면 j 를 만든 이전 개수와 새롭게 만들수 있는 개수의 최소값이므로 
dp[j] = min(dp[j], 1 + dp[j - coins[i]])

만들어질 수 없는 경우도 생각
=> 오답나옴
"""


def solution1():
    dp = [sys.maxsize for _ in range(k + 1)]
    for i in range(n):
        for j in range(1, k + 1):
            if i == 0 and j % coins[i] == 0:
                dp[j] = j // coins[i]
                continue

            if coins[i] > j:
                continue
            elif coins[i] == j:
                dp[j] = 1
            else:
                dp[j] = min(dp[j], 1 + dp[j - coins[i]])

    if dp[-1] == sys.maxsize:
        return -1
    return dp[-1]


"""
다른 답 보고 초기값 변경했더니 정답
만들어질수 없는 경우를 구분할 필요 없이 초기값을 maxsize 로 설정한다면
만들어질 수 없는 값들을 sys.maxsize 이기 때문에 알아서 최대값으로 처리
"""


def solution2():
    dp = [sys.maxsize for _ in range(k + 1)]
    dp[0] = 0

    for coin in coins:
        for i in range(coin, k + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[-1] == sys.maxsize:
        return -1
    return dp[-1]


"""
dp[0] 을 설정하는 이유는 coin == i 일 때 dp[i - coin] 값이 0 이 되도록 하려고
"""

print(solution0())
