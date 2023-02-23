# 5_connecting_island
# https://school.programmers.co.kr/learn/courses/30/lessons/42861
from collections import defaultdict, deque


def solution0(n, costs):
    def connected(node1, node2):
        queue = deque()
        visited = [0 for _ in range(n)]
        queue.appendleft(node1)
        visited[node1] = 1
        while queue:
            node = queue.pop()
            for temp in connect_dict[node]:
                if temp == node2:
                    return True

                if not visited[temp]:
                    queue.appendleft(temp)
                    visited[temp] = 1

        return False

    answer = 0
    costs.sort(key=lambda x: x[2])
    connect_dict = defaultdict(list)

    for node1, node2, cost in costs:
        if not connected(node1, node2):
            connect_dict[node1].append(node2)
            connect_dict[node2].append(node1)
            answer += cost

    return answer


"""
cost 가 작은 것부터 순회하면서 node1 에서 node2 까지 갈 수 있는지 확인. 연결되어 있는 지 확인할 때 bfs 사용
갈 수 있으면 connect_dict 에 추가하지 않고, 갈 수 없다면 connect_dict 에 추가한 후 answer 에 cost 더한다.
"""


def solution1(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    link = set([costs[0][0]])  # 시작 연결점 추가

    while len(link) != n:
        for island1, island2, cost in costs:
            if island1 in link and island2 in link:
                continue
            if island1 in link or island2 in link:
                answer += cost
                link.update([island1, island2])
                break

    return answer


"""
len(link) 가 n 이 되면 모두 연결되었다는 뜻이다.  모두 연결될 때까지 아래를 반복한다.
island1 과 island2 가 이미 연결되어 있다면 continue
island1 과 island2 중 하나만 연결되어 있다면 link 에 추가하고 비용을 더한다.
"""


def solution2(n, costs):
    def find(node):  # 재귀를 통해 node 의 부모 노드를 찾는다
        if parent[node] == node:
            return node
        return find(parent[node])

    def union(node1, node2):  # 두 집합을 합친다. 이때 더 작은 값이 항상 부모가 되도록 한다
        p1 = find(node1)
        p2 = find(node2)
        if p1 > p2:
            parent[p1] = p2
        else:
            parent[p2] = p1

    answer = 0
    parent = [i for i in range(n)]
    costs.sort(key=lambda x: x[2])
    for island1, island2, cost in costs:
        if find(island1) != find(island2):  # 섬끼리 연결 안됨
            union(island1, island2)
            answer += cost

    return answer


"""
크루스칼 알고리즘으로 연결되어있는지 확인할 때 union find 를 사용
union find 란? https://chiefcoder.tistory.com/55
그래프에서 한 노드와 다른 노드의 연결 여부를 파악할 때 사용하는 기법으로 특정 노드의 부모 노드를 찾는 find 와 
두 노드의 집합을 하나로 합치는 union 연산을 사용한다.

cost 가 작은 것 부터 순회하며 island1, island2 의 부모노드가 같지 않다면 연결되어있지 않으므로 union 해주고 cost 를 추가한다.
"""

n = 4
costs = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
print(solution1(n, costs))
