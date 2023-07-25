# 15989_1,2,3_더하기_4_Silver1
# https://www.acmicpc.net/problem/15989
T = int(input())
nums = [int(input()) for _ in range(T)]


def solution0():
    dp = [[0 for _ in range(10001)] for _ in range(3)]
    dp[0][1] = 1
    dp[0][2] = 1
    dp[1][2] = 1
    dp[0][3] = 1
    dp[1][3] = 1
    dp[2][3] = 1

    max_num = max(nums)
    for i in range(4, max_num + 1):
        dp[0][i] = dp[0][i - 1]
        dp[1][i] = dp[0][i - 2] + dp[1][i - 2]
        dp[2][i] = dp[0][i - 3] + dp[1][i - 3] + dp[2][i - 3]

    for num in nums:
        print(dp[0][num] + dp[1][num] + dp[2][num])


"""
부분문제로 나뉨 + 지난 값들을 사용 + dp 문제 -> 점화식과 dp 에 무엇을 저장할 지 정의해야함
겹치는 걸 어떻게 해결? => dp[3][T] 배열 사용하면 중복 제외하고 셀 수 있음
i 행의 배열은 i 이하의 값만 사용하여 구성 (ex 2 행은 1, 2 만 사용함)
dp[0][j] = dp[0][j-1]
dp[1][j] = dp[0][j-2] + dp[1][j-2]
dp[2][j] = dp[0][j-3] + dp[1][j-3] + dp[2][j-3]
"""


def solution1():
    dp = [1] * 10001

    for i in range(2, 10001):
        dp[i] += dp[i - 2]

    for i in range(3, 10001):
        dp[i] += dp[i - 3]

    for num in nums:
        print(dp[num])


"""
비슷한 방식이지만 좀 더 간단한 식으로 풀이 가능
모든 수는 1만써서 합 나타내는 방법 하나 잇음
2 가 추가되는 경우는 기존 값에 dp[i-2] 더해줌
3 이 추가되는 경우는 기존 값이 dp[i-3] 더해줌
"""

solution0()
