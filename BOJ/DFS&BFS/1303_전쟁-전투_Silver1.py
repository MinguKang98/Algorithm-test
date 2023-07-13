# 1303_전쟁-전투_Silver1
# https://solved.ac/search?query=1303
from collections import deque

N, M = map(int, input().split())
soldiers = []
for _ in range(M):
    soldiers.append(list(input()))


def solution0():
    visited = [[0 for _ in range(N)] for _ in range(M)]

    def dfs(color, cur_row, cur_col):
        if cur_row < 0 or cur_row >= M or cur_col < 0 or cur_col >= N:
            return 0

        if soldiers[cur_row][cur_col] != color:
            return 0

        if visited[cur_row][cur_col]:
            return 0

        temp = 1
        visited[cur_row][cur_col] = 1
        temp += dfs(color, cur_row + 1, cur_col)
        temp += dfs(color, cur_row - 1, cur_col)
        temp += dfs(color, cur_row, cur_col + 1)
        temp += dfs(color, cur_row, cur_col - 1)

        return temp

    white_list = []
    blue_list = []
    for i in range(M):
        for j in range(N):
            if not visited[i][j]:
                if soldiers[i][j] == 'W':
                    white_list.append(dfs('W', i, j))
                else:
                    blue_list.append(dfs('B', i, j))

    print(sum([w ** 2 for w in white_list]), sum([b ** 2 for b in blue_list]))


"""
같은 병사가 가로, 세로로 연결되면 뭉침
아군 W, 적군 B

dfs 로 푸는 방법
"""


def solution1():
    visited = [[0 for _ in range(N)] for _ in range(M)]

    def bfs(color, cur_row, cur_col):
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        queue = deque()
        queue.appendleft((cur_row, cur_col))
        visited[cur_row][cur_col] = 1
        temp = 1

        while queue:
            x, y = queue.pop()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < M and 0 <= ny < N:
                    if soldiers[nx][ny] == color and not visited[nx][ny]:
                        visited[nx][ny] = 1
                        queue.appendleft((nx, ny))
                        temp += 1

        return temp

    white_list = []
    blue_list = []
    for i in range(M):
        for j in range(N):
            if not visited[i][j]:
                if soldiers[i][j] == 'W':
                    white_list.append(bfs('W', i, j))
                else:
                    blue_list.append(bfs('B', i, j))

    print(sum([w ** 2 for w in white_list]), sum([b ** 2 for b in blue_list]))


"""
bfs 로 푸는 법
"""

solution1()
