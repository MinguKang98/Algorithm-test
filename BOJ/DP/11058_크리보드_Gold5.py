# 11058_크리보드_Gold5
# https://www.acmicpc.net/problem/11058

N = int(input())


def solution0():
    dp = [[0 for _ in range(N + 1)] for _ in range(4)]

    dp[0][1] = 1
    dp[3][1] = 1
    dp[0][2] = 2
    dp[1][2] = 1
    dp[3][2] = 2

    for i in range(3, N + 1):
        dp[0][i] = i
        dp[1][i] = dp[3][i - 1]
        dp[2][i] = dp[1][i - 1]
        dp[3][i] = max(dp[0][i], dp[2][i - 1] * 2, dp[3][i - 1] * 2 - dp[3][i - 2])
        print(dp)

    return dp[-1][-1]


"""
백트래킹도 생각했지만 부분값들을 활용해야 함 -> dp
dp 에 무엇을 저장 + dp 행렬 어떻게 구성 + 점화식은?
1. A 최대 갯수
2. 4*n 행렬. 행에는 버튼 값들, 열은 횟수.
dp[0][i] 는 A 버튼만 사용해서 만들 수 잇는 A 수
dp[1][i] 는 A + 전체 선택
dp[1][i] 는 A + 전체 선택, 복사, 즉 복사한 A 수 저장
dp[3][i] 는 모든 버튼을 사용해서 만들 수 있는 최대 A 수를 저장

3.
dp[0][i] = dp[3][i]+1 
dp[1][i] = dp[3][i-1]
dp[2][i] = dp[1][i-1]
dp[3][i] = max(dp[0][i], dp[2][i-1] * 2, dp[3][i-1]*2-dp[3][i-2])
마지막의 경우 A만 눌렀을 때, 복사해왔던거 붙여 넣을때, 이전거 븥여 넣을 때 중 최대

이전에 복사한 거 어떻게 관리??
=> 오답
"""


def solution1():
    dp = [i for i in range(N + 1)]
    if N < 6:
        return dp[N]

    for i in range(6, N + 1):
        dp[i] = max(dp[i - 3] * 2, dp[i - 4] * 3, dp[i - 5] * 4)
    return dp[-1]


"""
6까지는 A 연속입력이 가장 큼
6이후는 복붙을 적용한 값들을 비교. 
복사에 3번 커맨드 필요하므로 복사 한번, 두번, 세번 누른 경우를 비교하면 됨
"""


def solution2():
    dp = [i for i in range(N + 1)]
    if N < 6:
        return dp[N]

    for i in range(6, N + 1):
        for j in range(i - 3, -1, -1):
            dp[i] = max(dp[i], dp[j] * (i - j - 1))
    return dp[-1]


"""
범위가 작아 모든 복사 횟수에 대해 루프 돌려도 됨
현실적으로 이 방식으로 접근할 수 있을 듯
"""

print(solution0())
