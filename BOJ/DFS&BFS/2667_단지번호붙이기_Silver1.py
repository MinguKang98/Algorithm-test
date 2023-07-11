# 2667_단지번호붙이기_Silver1
# https://www.acmicpc.net/problem/2667
from collections import deque

N = int(input())
maps = []
for _ in range(N):
    maps.append(list(map(int, list(input()))))


def solution0():
    visited = [[0 for _ in range(N)] for _ in range(N)]

    def dfs(x, y):
        visited[x][y] = 1
        temp = 1
        if x + 1 < N:
            if maps[x + 1][y] == 1 and not visited[x + 1][y]:
                temp += dfs(x + 1, y)
        if x - 1 >= 0:
            if maps[x - 1][y] == 1 and not visited[x - 1][y]:
                temp += dfs(x - 1, y)
        if y + 1 < N:
            if maps[x][y + 1] == 1 and not visited[x][y + 1]:
                temp += dfs(x, y + 1)
        if y - 1 >= 0:
            if maps[x][y - 1] == 1 and not visited[x][y - 1]:
                temp += dfs(x, y - 1)

        return temp

    result = []
    for i in range(N):
        for j in range(N):
            cur = maps[i][j]
            if cur == 1 and not visited[i][j]:
                result.append(dfs(i, j))

    print(len(result))
    result.sort()
    for r in result:
        print(r)


"""
그래프 순회 -> dfs 가 쓰기 편해 보임
dfs 를 통해 단지내 집의 수를 반환한다.
"""
count = 0


def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False

    if maps[x][y] == 1:
        global count
        count += 1
        maps[x][y] = 0  # visited 사용 대신 maps 자체를 0으로 갱신
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False


def solution1():
    result = []
    global count

    for i in range(N):
        for j in range(N):
            if dfs(i, j):
                result.append(count)
                count = 0

    print(len(result))
    result.sort()
    for r in result:
        print(r)


"""
dfs 다른 방법
global 변수 count 를 사용하고 이전 dfs 와 처리 시점이 다르다
"""


def solution2():
    def bfs(x, y):
        queue = deque()
        queue.append([x, y])
        cnt = 0

        while queue:
            x, y = queue.pop()
            if x < 0 or x >= N or y < 0 or y >= N:
                continue

            if maps[x][y] == 1:
                cnt += 1
                maps[x][y] = 0  # visited 사용 대신 maps 자체를 0으로 갱신
                queue.appendleft([x + 1, y])
                queue.appendleft([x - 1, y])
                queue.appendleft([x, y + 1])
                queue.appendleft([x, y - 1])

        return cnt

    result = []
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 1:
                result.append(bfs(i, j))

    print(len(result))
    result.sort()
    for r in result:
        print(r)


"""
bfs 풀이


visited 를 사용하지 않은 방법. 사용해서 풀 수도 있을 듯
"""

solution2()
