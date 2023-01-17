# 3_network
# https://school.programmers.co.kr/learn/courses/30/lessons/43162
from collections import deque


def solution0(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]

    for i in range(n):
        if not visited[i]:
            # dfs
            stack = deque()
            stack.append(i)
            while stack:
                cur = stack.pop()
                visited[cur] = 1
                for j in range(n):
                    if i == j:
                        continue

                    if computers[cur][j] and not visited[j]:
                        stack.append(j)
            answer += 1
    return answer


"""
dfs 여러번 해서 dfs 횟수 세기
"""


# n = 3
# computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

print(solution0(n, computers))
