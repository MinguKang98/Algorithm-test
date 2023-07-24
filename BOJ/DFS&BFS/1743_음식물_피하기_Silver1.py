# 1743_음식물_피하기_Silver1
# https://www.acmicpc.net/problem/1743
import sys
from collections import deque

sys.setrecursionlimit(10000000)

N, M, K = map(int, input().split())
space = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
for _ in range(K):
    r, c = map(int, input().split())
    space[r][c] = 1


def solution0():
    def dfs(i, j):
        if i < 1 or i > N or j < 1 or j > M:
            return 0

        if not space[i][j]:
            return 0

        space[i][j] = 0
        return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)

    def dfs2(i, j):
        result = 1
        space[i][j] = 0
        if 1 < i <= N and 1 <= j <= M and space[i - 1][j]:
            result += dfs2(i - 1, j)
        if 1 <= i < N and 1 <= j <= M and space[i + 1][j]:
            result += dfs2(i + 1, j)
        if 1 <= i <= N and 1 < j <= M and space[i][j - 1]:
            result += dfs2(i, j - 1)
        if 1 <= i <= N and 1 <= j < M and space[i][j + 1]:
            result += dfs2(i, j + 1)
        return result

    answer = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if space[i][j]:
                answer = max(answer, dfs(i, j))

    return answer


"""
dfs 로 음식물 개수 찾기
정답인데 sys.setrecursionlimit(10000000) 안넣어서 오답처리 되었음
+ python3 로는 정답인데 pypy3 로는 오답;;
"""


def solution1():
    def bfs(i, j):
        result = 0
        queue = deque()
        queue.appendleft((i, j))

        while queue:
            r, c = queue.pop()
            if r < 1 or r > N or c < 1 or c > M:
                continue

            if not space[r][c]:
                continue

            space[r][c] = 0
            result += 1
            queue.appendleft((r - 1, c))
            queue.appendleft((r + 1, c))
            queue.appendleft((r, c - 1))
            queue.appendleft((r, c + 1))

        return result

    def bfs2(i, j):
        result = 1
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        queue = deque()
        queue.appendleft((i, j))
        space[i][j] = 0

        while queue:
            r, c = queue.pop()

            for d in range(4):
                nx, ny = r + dx[d], c + dy[d]
                if 0 < nx <= N and 0 < ny <= M and space[nx][ny]:
                    queue.appendleft((nx, ny))
                    space[nx][ny] = 0
                    result += 1
        return result

    answer = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if space[i][j]:
                answer = max(answer, bfs(i, j))

    return answer


"""
bfs 로도 풀이 가능
"""

print(solution1())
