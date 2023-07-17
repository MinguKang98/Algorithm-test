# 1197_최소_스패닝_트리_Gold4
# https://www.acmicpc.net/problem/1197
from collections import defaultdict
import heapq

V, E = map(int, input().split())
edges = []
for _ in range(E):
    edges.append(list(map(int, input().split())))


def solution1():
    def find(node):
        if node != v_root[node]:
            v_root[node] = find(v_root[node])  # 루트 찾으면서 갱신
        return v_root[node]

    answer = 0
    v_root = [i for i in range(V + 1)]
    edges.sort(key=lambda x: x[2])
    for src, dst, weight in edges:
        src_root = find(src)  # 루트 찾기
        dst_root = find(dst)

        if src_root != dst_root:  # 루트 다르면 연결. 두 루트 중 작은 루트를 선택
            if src_root > dst_root:
                v_root[src_root] = dst_root
            else:
                v_root[dst_root] = src_root
            answer += weight

    return answer


"""
MST 문제 -> 크루스칼/프림 사용해야함
크루스칼 핵심은 엣지를 가중치 오름차순으로 정렬 후 노드간의 루트 노드를 찾아 다르면 연결
v_root 는 root 저장하는 리스트. 처음엔 자기 자신이 루트, 갱신 시 작은 루트를 선택
시간복잡도 O(ElogE) 이므로 간선 적을 때 유리
"""


def solution2():
    visited = [0 for _ in range(V + 1)]
    edge_list = defaultdict(list)
    for src, dst, weight in edges:
        edge_list[src].append([weight, dst])
        edge_list[dst].append([weight, src])

    answer = 0
    cnt = 0
    heap = [[0, 1]]  # 특정 노드와 연결된 노드 중 방문하지 않은 노드 가중치 오름차순으로 보관

    while heap:
        if cnt == V:  # V 번 선택하면 MST 완성
            break

        weight, node = heapq.heappop(heap)
        if not visited[node]:
            visited[node] = 1
            answer += weight
            cnt += 1
            for i in edge_list[node]:  # 선택한 노드와 연결된 노드들 heap 으로 넣기
                heapq.heappush(heap, i)

    return answer


"""
크루스칼 핵심은 노드 집합에서 연결된 노드 중 가장 작은 가중치 가진 노드를 선택
이때 가중치 작은 거 우선 선택 위해 우선순위 큐 사용
시간복잡도 O(ElogV) 이므로 간선 많을 때 유리
"""

print(solution1())
