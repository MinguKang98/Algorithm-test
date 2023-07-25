# 2606_바이러스_Silver3
# https://www.acmicpc.net/problem/2606
from collections import defaultdict, deque

N = int(input())
M = int(input())
computers = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    computers[a].append(b)
    computers[b].append(a)


def solution0():
    visited = [0 for _ in range(N + 1)]

    def dfs(node):
        result = 1
        for computer in computers[node]:
            if not visited[computer]:
                visited[computer] = 1
                result += dfs(computer)

        return result

    visited[1] = 1

    return dfs(1) - 1


"""
1 에 연결된 노드 수 구하기
dfs 풀이
"""


def solution1():
    visited = [0 for _ in range(N + 1)]
    result = 0

    queue = deque()
    queue.appendleft(1)
    visited[1] = 1

    while queue:
        node = queue.pop()
        for computer in computers[node]:
            if not visited[computer]:
                visited[computer] = 1
                queue.appendleft(computer)
                result += 1

    return result


"""
bfs 풀이
"""

print(solution1())
