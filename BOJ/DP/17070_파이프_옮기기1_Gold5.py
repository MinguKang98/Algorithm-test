# 17070_파이프_옮기기1_Gold5
# https://solved.ac/search?query=17070

N = int(input())
houses = []
for _ in range(N):
    houses.append(list(map(int, input().split())))

answer = 0


def solution0():
    houses[0][0] = 2
    houses[0][1] = 2

    def dfs(cur_x, cur_y):  # 파이프 중 왼쪽 기준 좌표
        global answer

        if cur_x + 1 < N and cur_y < N:
            if houses[cur_x + 1][cur_y] == 2:  # 가로
                if cur_x + 1 == N - 1 and cur_y == N - 1:
                    answer += 1
                    return

                if cur_x + 2 < N and cur_y < N and houses[cur_x + 2][cur_y] != 1:  # 옆으로
                    houses[cur_x][cur_y] = 0
                    houses[cur_x + 2][cur_y] = 2
                    dfs(cur_x + 1, cur_y)
                    houses[cur_x][cur_y] = 2
                    houses[cur_x + 2][cur_y] = 0

                if cur_x + 2 < N and cur_y + 1 < N and (
                        houses[cur_x + 2][cur_y] + houses[cur_x + 1][cur_y + 1] + houses[cur_x + 2][
                    cur_y + 1]) == 0:  # 대각선
                    houses[cur_x][cur_y] = 0
                    houses[cur_x + 2][cur_y + 1] = 2
                    dfs(cur_x + 1, cur_y)
                    houses[cur_x][cur_y] = 2
                    houses[cur_x + 2][cur_y + 1] = 0

        if cur_x < N and cur_y + 1 < N:
            if houses[cur_x][cur_y + 1] == 2:  # 세로
                if cur_x == N - 1 and cur_y + 1 == N - 1:
                    answer += 1
                    return

                if cur_x < N and cur_y + 2 < N and houses[cur_x][cur_y + 2] != 1:  # 아래로
                    houses[cur_x][cur_y] = 0
                    houses[cur_x][cur_y + 2] = 2
                    dfs(cur_x, cur_y + 1)
                    houses[cur_x][cur_y] = 2
                    houses[cur_x][cur_y + 2] = 0

                if cur_x + 1 < N and cur_y + 2 < N and (
                        houses[cur_x + 1][cur_y + 1] + houses[cur_x][cur_y + 2] + houses[cur_x + 1][
                    cur_y + 2]) == 0:  # 대각선
                    houses[cur_x][cur_y] = 0
                    houses[cur_x + 1][cur_y + 2] = 2
                    dfs(cur_x, cur_y + 1)
                    houses[cur_x][cur_y] = 2
                    houses[cur_x + 1][cur_y + 2] = 0

        if cur_x + 1 < N and cur_y + 1 < N:
            if houses[cur_x + 1][cur_y + 1] == 2:  # 대각
                if cur_x + 1 == N - 1 and cur_y + 1 == N - 1:
                    answer += 1
                    return

                if cur_x + 2 < N and cur_y + 1 < N and houses[cur_x + 2][cur_y + 1] != 1:  # 옆으로
                    houses[cur_x][cur_y] = 0
                    houses[cur_x + 2][cur_y + 1] = 2
                    dfs(cur_x + 1, cur_y + 1)
                    houses[cur_x][cur_y] = 2
                    houses[cur_x + 2][cur_y + 1] = 0

                if cur_x + 1 < N and cur_y + 2 < N and houses[cur_x + 1][cur_y + 2] != 1:  # 아래로
                    houses[cur_x][cur_y] = 0
                    houses[cur_x + 1][cur_y + 2] = 2
                    dfs(cur_x + 1, cur_y + 1)
                    houses[cur_x][cur_y] = 2
                    houses[cur_x + 1][cur_y + 2] = 0

                if cur_x + 2 < N and cur_y + 2 < N and (houses[cur_x + 2][cur_y + 1] + houses[cur_x + 1][cur_y + 2] +
                                                        houses[cur_x + 2][cur_y + 2]) == 0:  # 대각선
                    houses[cur_x][cur_y] = 0
                    houses[cur_x + 2][cur_y + 2] = 2
                    dfs(cur_x + 1, cur_y + 1)
                    houses[cur_x][cur_y] = 2
                    houses[cur_x + 2][cur_y + 2] = 0

    dfs(0, 0)


"""
모든 경우를 확인해야 함
bfs/dfs vs dp => 이전 기록이 필요없음
백트래킹으로 풀어야 하는 듯
파이프 표현을 어떻게 해야하나
대각선일때 비어있어야 하는 부분 체크 안해서 예제 오류났음 => 수정
백트래킹으로 풀었는데 굳이 백트래키잉 필요한가 싶음
그리고 이전 기록이 필요없지 않음 -> 이전에 잘못 판단

90퍼에서 시간초과
"""


def solution1():
    def dfs(x, y, state):  # state 0: 가로, 1: 세로 , 2: 대각선
        if x == N - 1 and y == N - 1:
            answer += 1
            return

        if state == 0:
            if y == N - 1:  # 이동불가
                return

            if 0 <= x < N and 0 <= y + 1 < N and houses[x][y + 1] == 0:
                dfs(x, y + 1, 0)

            if 0 <= x + 1 < N and 0 <= y + 1 < N and houses[x][y + 1] == 0 and houses[x + 1][y] == 0 and houses[x + 1][
                y + 1] == 0:
                dfs(x + 1, y + 1, 2)

        elif state == 1:
            if x == N - 1:  # 이동불가
                return

            if 0 <= x + 1 < N and 0 <= y < N and houses[x + 1][y] == 0:
                dfs(x + 1, y, 1)

            if 0 <= x + 1 < N and 0 <= y + 1 < N and houses[x][y + 1] == 0 and houses[x + 1][y] == 0 and houses[x + 1][
                y + 1] == 0:
                dfs(x + 1, y + 1, 2)

        elif state == 2:
            if 0 <= x < N and 0 <= y + 1 < N and houses[x][y + 1] == 0:
                dfs(x, y + 1, 0)

            if 0 <= x + 1 < N and 0 <= y < N and houses[x + 1][y] == 0:
                dfs(x + 1, y, 1)

            if 0 <= x + 1 < N and 0 <= y + 1 < N and houses[x][y + 1] == 0 and houses[x + 1][y] == 0 and houses[x + 1][
                y + 1] == 0:
                dfs(x + 1, y + 1, 2)

    dfs(0, 1, 0)


"""
dfs 로 푸는 법
"""


def solution2():
    dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]

    dp[0][0][1] = 1  # 파이프 방향, 행, 열
    # 파이프 방향은 0 : 가로, 1 : 세로, 2 : 대각선
    for i in range(2, N):
        if houses[0][i] == 0:
            dp[0][0][i] = dp[0][0][i - 1]  # 파이프 가로일 때 1행 적용

    for i in range(1, N):
        for j in range(1, N):
            if houses[i][j] == 0:
                dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1]  # 가로
                dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]  # 세로

            if houses[i][j] == 0 and houses[i][j - 1] == 0 and houses[i - 1][j] == 0:
                dp[2][i][j] = dp[0][i - 1][j - 1] + dp[1][i - 1][j - 1] + dp[2][i - 1][j - 1]

    print(dp[0][N - 1][N - 1] + dp[1][N - 1][N - 1] + dp[2][N - 1][N - 1])


"""
dp로 푸는 법
dp에는 파이프 방향, 행, 열을 저장한다. 이때 행, 열은 파이프의 앞부분을 나타낸다.
dp[?][x][y] 가 의미하는 것은 현재 머리가 x, y에 위치한 ? 모양 파이프가 되기 까지의 경우의 수 

가로 세로는 현재 칸만, 대각선은 현재칸과 왼쪽, 위가 비어잇어야 함
가로가 되려면 이전에 가로와 대각선
세로가 되려면 이전에 세로와 대각선
대각선이 되려면 이전에 가로 세로 대각선


작은 부분문제들로 문제를 풀 수 있나 생각해보자
=> 이전까지의 경우의 수들로 현재 경우의 수 구할 수 있음
"""

print(answer)
