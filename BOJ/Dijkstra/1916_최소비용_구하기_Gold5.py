# 1916_최소비용_구하기_Gold5
# https://www.acmicpc.net/problem/1916
from collections import defaultdict
import heapq
import sys

N = int(input())
M = int(input())
buses = []
for _ in range(M):
    buses.append(list(map(int, input().split())))
start, end = map(int, input().split())


def solution1():
    bus_map = defaultdict(list)
    for bus in buses:
        bus_map[bus[0]].append([bus[1], bus[2]])

    cost_list = [sys.maxsize for _ in range(N + 1)]
    cost_list[start] = 0

    queue = []
    heapq.heappush(queue, [cost_list[start], start])
    while queue:
        cur_cost, cur_node = heapq.heappop(queue)

        if cost_list[cur_node] < cur_cost:  # 탐색할 노드의 거리가 기존보다 길면 무시
            continue

        for next_node, next_cost in bus_map[cur_node]:
            temp_cost = cur_cost + next_cost  # 다음 노드로 갈 때 비용
            if temp_cost < cost_list[next_node]:  # 다음노드로 갈 때 비용이 기존 비용보다 작으면 갱신
                cost_list[next_node] = temp_cost
                heapq.heappush(queue, [temp_cost, next_node])

    return cost_list[end]


print(solution1())

"""
dfs/bfs??
다익스트라가 적합하다고 판단 -> 유형 판단은 맞았는데 구현 못함

다익스트라
1. 출발 노드 설정
2. 출발 노드 기준 각 노드 최소비용 저장
3. 방문하지 않은 노드 중 가장 비용 적은 노드 선택
4. 해당 노드 거쳐서 특저한 노드 가는 경우 고려하여 최소 비용 갱신
5. 3 ~ 4 반복

python 의 경우 방문하지 않은 노드 중 가장 비용 적은 녿 선택하는 것을 heapq 사용하여 구현 가능
=> queue 에 들어간 노드 가장 짧은 노드가 아니면 우선순위가 뒤로 밀려나기 때문
"""
