# 2178_미로탐색_Silver1
# https://www.acmicpc.net/problem/2178
from collections import deque

N, M = map(int, input().split())
mazes = []
for _ in range(N):
    mazes.append(list(map(int, list(input()))))


def solution0():
    answer = 0
    visited = [[0 for _ in range(M)] for _ in range(N)]
    queue = deque()
    queue.appendleft((0, 0, 1))
    while queue:
        row, col, cost = queue.pop()
        if row < 0 or row >= N or col < 0 or col >= M:
            continue

        if visited[row][col] or not mazes[row][col]:
            continue

        if row == N - 1 and col == M - 1:
            answer = cost
            break

        visited[row][col] = 1
        queue.appendleft((row + 1, col, cost + 1))
        queue.appendleft((row - 1, col, cost + 1))
        queue.appendleft((row, col + 1, cost + 1))
        queue.appendleft((row, col - 1, cost + 1))

    return answer


"""
지나야 하는 최소 칸수 => bfs 무난
"""


def solution1():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and mazes[nx][ny] == 1:
                queue.appendleft((nx, ny))
                mazes[nx][ny] = mazes[x][y] + 1

    return mazes[N - 1][M - 1]


"""
maze 행 자체를 업데이트하는 방법
"""

print(solution1())
