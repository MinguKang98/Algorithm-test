# 2616_소형기관차_Gold3
# https://www.acmicpc.net/problem/2616


N = int(input())
guests = list(map(int, input().split()))
M = int(input())


def solution1():
    dp = [[0 for _ in range(N + 1)] for _ in range(4)]
    prefix = [0 for _ in range(N + 1)]
    for idx, guest in enumerate(guests):
        prefix[idx + 1] = prefix[idx] + guest

    for i in range(1, 4):
        for j in range(i * M, N + 1):  # 시작점이 i * M 은 맞았음
            if i == 1:
                dp[i][j] = max(dp[i][j - 1], prefix[j] - prefix[j - M])
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - M] + prefix[j] - prefix[j - M])

    return dp[3][N]


"""
소형기관차가 끄는 객차 최대 수 존재. 3대 모두 같다
최대한 많은 손님
번호가 연속적 (ex. 1,2 3,4 5,6)
=> 점화식 못 찾아서 답지 보기


dp 에 무엇을 넣어야 하나
=> 기차수 X 객차 수 & dp[i][j] 는 i 번째 소형기관차가 j 번째 객차까지 주어졌을 때 승객 최대값
점화식?
첫 소형기관차 : 현재까지 연속한 구간값과 이전 값 중 최대  
나머지 : (현재까지 연속한 구간값 + 연속하기 전 최대값) 과 이전 값 중 최대


구간합 + dp 문제. 구간 합을 쓸 생각을 못해 풀이를 못한듯
"""

print(solution1())
