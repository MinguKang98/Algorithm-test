# 1260_DFS와_BFS
# https://www.acmicpc.net/problem/1260
from collections import defaultdict, deque

n, m, v = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    src, dst = map(int, input().split())
    graph[src].append(dst)
    graph[dst].append(src)

for s in graph.keys():
    graph[s].sort()

visited1 = [0 for _ in range(n + 1)]
visited2 = [0 for _ in range(n + 1)]


def dfs(start, visited, path):
    path.append(start)
    visited[start] = 1
    for temp in graph[start]:
        if not visited[temp]:
            dfs(temp, visited, path)

    return ' '.join(map(str, path))


def bfs(start, visited, path):
    queue = deque()
    queue.appendleft(start)
    path.append(start)
    visited[start] = 1

    while queue:
        cur = queue.pop()
        for temp in graph[cur]:
            if not visited[temp]:
                queue.appendleft(temp)
                visited[temp] = 1
                path.append(temp)

    return ' '.join(map(str, path))


print(dfs(v, visited1, []))
print(bfs(v, visited2, []))
