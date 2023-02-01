# 6_dividing_electronic_network
# https://school.programmers.co.kr/learn/courses/30/lessons/86971
from collections import deque


def solution0(n, wires):
    def bfs(start, nodes):
        cnt = 0  # 송전탑 수
        visited = [0 for _ in range(n + 1)]
        queue = deque()
        queue.appendleft(start)
        while queue:
            cur = queue.pop()
            visited[cur] = 1
            cnt += 1
            for node in nodes:
                if cur == node[0] and not visited[node[1]]:
                    queue.appendleft(node[1])
                if cur == node[1] and not visited[node[0]]:
                    queue.appendleft(node[0])

        return cnt

    result = []
    for idx, wire in enumerate(wires):
        temp = wires[:]
        temp.pop(idx)

        length1 = bfs(wire[0], temp)
        length2 = bfs(wire[1], temp)

        result.append(abs(length1 - length2))

    return min(result)


"""
1. wires 중 끊을 wire 선택
2. 끊었을 때 생기는 두 전력망의 송전탑 갯수 및 차이 구하기 => 어떻게 갯수 구하나?? bfs 로 연결된 트리 탐색
3. 완전 탐색 후 최솟값이 정답 
"""


def solution1(n, wires):
    def dfs(start, nodes):
        cnt = 0  # 송전탑 수
        visited = [0 for _ in range(n + 1)]
        stack = deque()
        stack.append(start)
        while stack:
            cur = stack.pop()
            visited[cur] = 1
            cnt += 1
            for node in nodes:
                if cur == node[0] and not visited[node[1]]:
                    stack.append(node[1])
                if cur == node[1] and not visited[node[0]]:
                    stack.append(node[0])

        return cnt

    result = []
    for idx, wire in enumerate(wires):
        temp = wires[:]
        temp.pop(idx)

        length1 = dfs(wire[0], temp)
        length2 = dfs(wire[1], temp)

        result.append(abs(length1 - length2))

    return min(result)


"""
dfs 로도 탐색 가능
"""

n = 9
wires = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]

# n = 4
# wires = [[1, 2], [2, 3], [3, 4]]

# n = 7
# wires = [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]

print(solution0(n, wires))
