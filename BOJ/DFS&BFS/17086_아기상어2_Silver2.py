# 17086_아기상어2_Silver2
# https://www.acmicpc.net/problem/17086
from collections import deque

N, M = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(N)]


def solution0():
    def bfs(x, y):
        visited = [[0] * M for _ in range(N)]
        queue = deque()
        queue.appendleft((x, y, 0))
        visited[x][y] = 1

        result = 0
        while queue:
            cur_x, cur_y, cost = queue.pop()
            if space[cur_x][cur_y] == 1:
                result = cost
                break

            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
                nx = cur_x + dx
                ny = cur_y + dy
                if 0 <= nx < N and 0 <= ny < M:
                    if not visited[nx][ny]:
                        visited[nx][ny] = 1
                        queue.appendleft((nx, ny, cost + 1))

        return result

    temp = []
    for i in range(N):
        for j in range(M):
            if space[i][j] == 0:
                temp.append(bfs(i, j))
            else:
                temp.append(1)
    return max(temp)


"""
칸마다 상어사이의 거리 최소값 구하기 -> 그 칸의 안전거리 
-> 칸마다 bfs 로 안전거리 구하기
그 값들의 최대값
-> 안전거리들의 max 

visited[nx][ny] = 1 대신 visited[nx][ny] = visited[cur_x][cur_y] + 1 을 사용하면
거리를 visited 안에 저장 가능
"""


def solution1():
    queue = deque()
    for i in range(N):
        for j in range(M):
            if space[i][j] == 1:
                queue.appendleft((i, j))

    while queue:
        cur_x, cur_y = queue.pop()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
            nx = cur_x + dx
            ny = cur_y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if space[nx][ny] == 0:
                    space[nx][ny] = space[cur_x][cur_y] + 1
                    queue.appendleft((nx, ny))

    result = 0
    for i in range(N):
        for j in range(M):
            result = max(result, space[i][j])
    return result - 1


"""
칸 기준 상어까지의 거리가 아닌, 상어 기준 칸까지의 거리 계산
상어 위치를 큐에 넣은 후, 상어에 대해서 bfs 를 사용해
지나가지 않았다면, space 의 칸마다 상어로부터의 거리를 넣어줌
이후 space 의 최대값에서 1을 뺀 값이 정답
"""

print(solution1())
