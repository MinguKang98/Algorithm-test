# HSAT6_츨퇴근길
# https://softeer.ai/practice/info.do?idx=1&eid=1529
from collections import defaultdict, deque

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
S, T = map(int, input().split())


def solution0():
    edge_dict = defaultdict(list)
    for s, d in edges:
        edge_dict[s].append(d)
    go_nodes = [0 for _ in range(n + 1)]
    back_nodes = [0 for _ in range(n + 1)]

    def bfs(start, end, visited):
        queue = deque()
        queue.appendleft(start)
        visited[start] = 1

        while queue:
            cur_node = queue.pop()
            if cur_node == end:
                continue

            for next_node in edge_dict[cur_node]:
                if next_node == start:
                    queue.appendleft(next_node)

                if not visited[next_node]:
                    visited[next_node] = 1
                    queue.appendleft(next_node)

    bfs(S, T, go_nodes)
    bfs(T, S, back_nodes)
    go_nodes[S] = 0
    go_nodes[T] = 0
    back_nodes[S] = 0
    back_nodes[T] = 0

    result = 0
    for i in range(1, n + 1):
        if go_nodes[i] and back_nodes[i]:
            result += 1

    return result


"""
출근, 퇴근 방문 노드 체크
겹치는 개수 return
=> 오답 => 출근길에는 S를, 퇴근길에는 T 를 여러번 들러도 되는데 해당 부분 고려 ㄴㄴ
=> 오답 => 시작 노드뿐만 아니라 사이클 돌고 온 경우에 대해서도 생각해야함
-> 방문했다고 가는 거 아님
"""


def solution1():
    edge_dict = defaultdict(list)
    reverse_edge_dict = defaultdict(list)
    for s, d in edges:
        edge_dict[s].append(d)
        reverse_edge_dict[d].append(s)

    def dfs(cur_node, adj, visited):
        if visited[cur_node] == 1:
            return
        else:
            visited[cur_node] = 1
            for node in adj[cur_node]:
                dfs(node, adj, visited)

    from_s = [0] * (n + 1)
    from_s[T] = 1
    dfs(S, edge_dict, from_s)

    from_t = [0] * (n + 1)
    from_t[S] = 1
    dfs(T, edge_dict, from_t)

    to_s = [0] * (n + 1)
    dfs(S, reverse_edge_dict, to_s)

    to_t = [0] * (n + 1)
    dfs(T, reverse_edge_dict, to_t)

    result = 0
    for i in range(1, n + 1):
        if from_s[i] and from_t[i] and to_s[i] and to_t[i]:
            result += 1

    return result - 2


"""
간선 방햔 반대로 가는 거를 생각
edge_dict[i] 가 i 에서 갈 수 있는 노드 표현이라면
reverse_edge_dict[i] 는  i 에 올 수 있는 노드들 표현

S와 T에서 특정 지점 i까지 갈 수 있는지 from_s 와 from_t 를 edge_dict 을 통한 dfs 로 파악한다면
특정 지점 i 에서 S와 T까지 갈 수 있는지는 to_s 와 to_t 를 reverse_edge_dict 을 통한 dfs 로 파악

from_s[i], from_t[i], to_s[i], to_t[i] 이 모두 1이라면 i 는 출퇴근 모두 방문하는 노드이다
"""

print(solution1())
