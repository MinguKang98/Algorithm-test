# 15486_퇴사2_Gold5
# https://www.acmicpc.net/problem/15486

N = int(input())
data_list = [list(map(int, input().split())) for _ in range(N)]  # [시간 비용]


def solution0():
    dp = [0 for _ in range(N + 1)]

    for i in range(1, N + 1):
        time, cost = data_list[i - 1]
        if i + time - 1 <= N:
            dp[i + time - 1] = max(dp[i + time - 1], dp[i - 1] + cost)
        dp[i] = max(dp[i - 1], dp[i])

    return dp[-1]


"""
상담 기간은 당일 포함
지금 dp 를 과거를 통해 계산 vs 미래 dp 를 지금을 통해 계산 => 헷갈려서 해결 예시 참조
=> dp[i] 는 i일까지의 최대 이익이고 미래 dp 를 지금을 통해 계산해야 함
또한 dp[i] 는 갱신이 안될 수 있으므로 dp[i-1] 과 dp[i] 중 최대값으로 설정

점화식 : dp[i + time - 1] = max(dp[i + time - 1], dp[i - 1] + cost)
"""

print(solution0())
