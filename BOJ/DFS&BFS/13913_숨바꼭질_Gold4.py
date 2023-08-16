# 13913_숨바꼭질_Gold4
# https://www.acmicpc.net/problem/13913
from collections import deque

N, K = map(int, input().split())


def solution0():
    visited = [0 for _ in range(100001)]
    queue = deque()
    queue.appendleft((N, [N]))
    visited[N] = 1

    result = []
    while queue:
        cur, path = queue.pop()
        if cur == K:
            result = path
            break

        for dx in (1, -1, cur):
            nx = cur + dx
            if 0 <= nx <= 100000 and not visited[nx]:
                visited[nx] = 1
                temp = path[:]
                temp.append(nx)
                queue.appendleft((nx, temp))

    print(len(result) - 1)
    print(' '.join(map(str, result)))


"""
x 에서 1초 후 x+1 or x-1 or 2*x
가장 빠르게 도착하는 시간 

dfs/백트래킹 불가 -> 하한선 없어서 안끊김
bfs -> 원하는 값 나오면 종료

메모리초과 => 배열 복사 말고 다른 방법 없나
"""


def solution1():
    visited = [0 for _ in range(100001)]
    pre_nodes = [0 for _ in range(100001)]
    queue = deque()
    queue.appendleft((N, 0))
    visited[N] = 1

    def path(node, time):
        arr = []
        temp = node
        for _ in range(time + 1):
            arr.append(temp)
            temp = pre_nodes[temp]
        return ' '.join(map(str, arr[::-1]))

    while queue:
        cur, time = queue.pop()
        if cur == K:
            print(time)
            print(path(cur, time))
            break

        for nx in (cur + 1, cur - 1, cur * 2):
            if 0 <= nx <= 100000 and not visited[nx]:
                visited[nx] = 1
                pre_nodes[nx] = cur
                queue.appendleft((nx, time + 1))


"""
이전에 지난 값을 저장하는 배열 생성 => pre_nodes
pre_node[x]=y 는 x 를 지나기 전 y 를 거쳤다는 뜻
"""


def solution2():
    times = [0 for _ in range(100001)]
    pre_nodes = [0 for _ in range(100001)]
    queue = deque()
    queue.appendleft(N)

    def path(node):
        arr = []
        temp = node
        for _ in range(times[node] + 1):
            arr.append(temp)
            temp = pre_nodes[temp]
        return ' '.join(map(str, arr[::-1]))

    while queue:
        cur = queue.pop()
        if cur == K:
            print(times[cur])
            print(path(cur))
            break

        for nx in (cur + 1, cur - 1, cur * 2):
            if 0 <= nx <= 100000 and not times[nx]:
                times[nx] = times[cur] + 1
                pre_nodes[nx] = cur
                queue.appendleft(nx)


"""
solution1 과 같지만, bfs 에 time 을 저장하지 않고 visited 에 time 을 저장
"""

solution2()
