# 2281_데스노트_Gold3
# https://www.acmicpc.net/problem/2281
import sys

n, m = map(int, input().split())
notes = [int(input()) for _ in range(n)]


def solution0():
    dp = [[sys.maxsize for _ in range(m + 1)] for _ in range(n)]
    dp[0][notes[0]] = (m - notes[0]) ** 2
    for i in range(1, n):
        for j in range(1, m + 1):
            if dp[i - 1][j] != sys.maxsize:
                dp[i][notes[i]] = min(dp[i][notes[i]], dp[i - 1][j] + (m - notes[i]) ** 2)
                if j + notes[i] + 1 <= m:
                    dp[i][j + notes[i] + 1] = \
                        min(dp[i][j + notes[i] + 1], dp[i - 1][j] - (m - j) ** 2 + (m - j - notes[i] - 1) ** 2)
    for j in range(1, m + 1):
        if dp[n - 1][j] != sys.maxsize:
            dp[n - 1][j] = dp[n - 1][j] - (m - j) ** 2

    return min(dp[n - 1])


"""
위에서 아래, 왼쪽에서 오른쪽
사람마다 한칸, 잘리지 않음
남은 칸의 제곱의 합이 최소가 되도록. 마지막 줄은 계산 ㄴㄴ

dp 에 무엇을 저장?
행에는 이름 길이의 인덱스, 현재 길이
<= 처음에 행에는 줄의 수로 생각했는데 아닌 듯 해서 포기

점화식? 
이전 행을 탐색하며 이름을 이어서 할지 다음줄로 갈지 결정
다음 줄의 경우 : dp[i][notes[i]] = dp[i-1][j] + (m - notes[i]) ** 2
잇는 경우 : dp[i][j + notes[i] + 1] = dp[i-1][j] - (m - j)**2 + (m - j - notes[i] - 1)**2
위의 식처럼 계산하면 마지막 줄 제곱합까지 계산하므로 마지막 줄은 빼줌


이전 줄 존재하면 조건 분기해서 현재 줄 계산하는 dp 문제! 
"""


def solution1():
    maxNum = m * m * n
    dp = [maxNum] * (n + 1)
    dp[n] = 0

    def note(index: int):
        if dp[index] < maxNum:
            return dp[index]

        remain = m - notes[index]

        for i in range(index + 1, n + 1):  # 다음 이름 길이부터 탐색
            if remain >= 0:
                if i == n:
                    dp[index] = 0
                    break
                dp[index] = min(dp[index], remain * remain + note(i))
                remain -= notes[i] + 1

        return dp[index]

    return note(0)


"""
재귀 사용 + 1차원 dp 로 풀이한 답안
solution0 은 bottom-up 방식인 반면 위 풀이는 top-down 방식

"""

print(solution1())
