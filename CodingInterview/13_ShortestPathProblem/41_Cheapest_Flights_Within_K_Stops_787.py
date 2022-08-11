# 41_Cheapest_Flights_Within_K_Stops_787
import sys
from collections import defaultdict
import heapq
from typing import List
from collections import deque


class Solution:
    # Solution0 - using bfs and not clear
    def findCheapestPrice0(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:  # 출발, 도착, 비용
            graph[u].append([v, w, 0])  # [도착, 비용, 경유 횟수]

        cost_list = [sys.maxsize] * n  # 비용 리스트
        count_list = [-1] * n  # 경유 횟수 리스트
        cost_list[src] = 0
        queue = deque()  # 방문할 큐
        queue.append(src)

        while queue:
            print("cost: ", cost_list)
            print("count: ", count_list)
            node = queue.popleft()
            for end, cost, count in graph[node]:
                if cost_list[node] + cost < cost_list[end] and count_list[node] < k:
                    cost_list[end] = cost_list[node] + cost
                    count_list[end] = count_list[node] + 1
                    queue.append(end)

        return -1 if (cost_list[dst] == sys.maxsize) else cost_list[dst]

    """
    대부분은 통과하지만, 경유해야하는 노드의 count가 초기화 되는 경우 실패
    """

    # Solution1 - using daijkstra's algorithm and min heap
    def findCheapestPrice1(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:  # 출발, 도착, 비용
            graph[u].append((v, w))  # (도착, 비용)

        Q = [(0, src, -1)]  # (비용, 출발, 경유)

        while Q:
            price, node, count = heapq.heappop(Q)
            if node == dst:
                return price
            if count < k:
                count += 1
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, count))
        return -1

    # Solution2 - using daijkstra's algorithm and min heap
    def findCheapestPrice2(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:  # 출발, 도착, 비용
            graph[u].append((v, w))  # (도착, 비용)

        Q = [(0, src, k)]  # (비용, 출발, 경유)

        while Q:
            price, node, count = heapq.heappop(Q)
            if node == dst:
                return price
            if count >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, count - 1))
        return -1

    """
    price를 기준으로 min heap을 사용하는 것은 40번과 유사
    경유 횟수를 추가하여 경유 욋수에 제한을 두어 수행
    Solution 1,2는 Time Limit Exceed 발생
    """

    # Solution3 - using daijkstra's algorithm and min heap
    def findCheapestPrice3(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        Q = [(0, src, 0)]
        count_list = [sys.maxsize] * n  #

        while Q:
            price, node, count = heapq.heappop(Q)
            if node == dst:
                return price
            if count > k or count >= count_list[node]:
                continue
            count_list[node] = count
            count += 1
            for v, w in graph[node]:
                alt = price + w
                heapq.heappush(Q, (alt, v, count))
        return -1

    """
    노드 까지 경유 횟수를 저장하는 count_list를 추가
    count > k 뿐만 아니라 node의 count가 count_list[node} 보다 큰 경우는 계산 ㄴㄴ
    """


n = 4
flights = [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]]
src = 0
dst = 3
k = 1

print(Solution().findCheapestPrice3(n, flights, src, dst, k))
