# 5557_1학년_Gold5
# https://www.acmicpc.net/problem/5557

N = int(input())
nums = list(map(int, input().split()))


def solution0():
    dp = [[0 for _ in range(21)] for _ in range(N - 1)]
    dp[0][nums[0]] = 1

    for i in range(1, N - 1):
        for j in range(21):
            if dp[i - 1][j] != 0:
                if 0 <= j + nums[i] <= 20:
                    dp[i][j + nums[i]] += dp[i - 1][j]
                if 0 <= j - nums[i] <= 20:
                    dp[i][j - nums[i]] += dp[i - 1][j]
    return dp[N - 2][nums[-1]]


"""
중간 계싼 결과는 항상 0이상 20이하
개수를 세야 함
dp 를  게산 결과(0~20) 과 계산할 숫자의 개수(N-1) 로 구성

bfs 도 가능할 거 같음 -> 풀이는 가능하나 찾아보니 시간초과 난다고함
"""

print(solution0())
