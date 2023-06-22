# 15591_MooTube(Silver)
# https://www.acmicpc.net/problem/15591
from collections import defaultdict, deque


def recommend(limit, src):
    cnt = 0
    visited = [0 for _ in range(N + 1)]
    usados = [1000000001 for _ in range(N + 1)]
    queue = deque()
    queue.append([src, 1000000001])

    while queue:
        cur, pre_usado = queue.pop()
        visited[cur] = 1
        for node, r in network[cur]:
            if not visited[node]:
                usados[node] = min(r, pre_usado)
                if usados[node] >= limit:
                    queue.appendleft([node, usados[node]])
                    cnt += 1  # queue 에 추가한 node 는 limit 이상이므로 카운트함

    return cnt


N, Q = map(int, input().split())
network = defaultdict(list)
for _ in range(N - 1):
    p, q, r = map(int, input().split())
    network[p].append([q, r])
    network[q].append([p, r])

for _ in range(Q):
    k, v = map(int, input().split())
    print(recommend(k, v))

"""
p, q, r 로 네트워크 구성
유사도가 k 이상인 동영상을 동영상 v 를 보고 있는 소들에게 몇 개 추천


임의의 두 쌍 사이의 유사도 -> 두 쌍의 모든 경로의 유사도 중 최소
dfs/bfs 를 사용할 듯


"""
