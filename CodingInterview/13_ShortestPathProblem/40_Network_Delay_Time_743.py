# 40_Network_Delay_Time_743

from collections import defaultdict
import heapq
from typing import List
import sys

class Solution:
    # Solution 0 - using bfs
    def networkDelayTime0(self, times: List[List[int]], n: int, k: int) -> int:
        queue=[k] # 방문할 노드 저장
        time_list=[sys.maxsize]*n # 소요시간 나타내는 list
        time_list[k-1]=0 # 시작 노드는 소요시간 0 

        graph=defaultdict(list)
        for u, v, w in times:
            graph[u].append((v,w))
            
        while queue:
            node=queue.pop()
            for dest, time in graph[node]:
                if time_list[node-1]+time < time_list[dest-1]:
                    time_list[dest-1]=time_list[node-1]+time
                    queue.append(dest)
        
        
        return -1 if (sys.maxsize in time_list) else max(time_list)

    # Solution 1 - using daijkstra's algorithm and min heap
    def networkDelayTime0(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        for u, v, w in times:
            graph[u].append((v,w))

        Q=[(0, k)] #[(소요시간,정점)]
        dist = defaultdict(int) # 거리 저장

        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))

        if len(dist)==n:
            return max(dict.values())
        return -1
        


# times = [[2,1,1],[2,3,1],[3,4,1]]
# n = 4
# k = 2

times = [[1,2,1]]
n = 2
k = 2

print(Solution().networkDelayTime0(times,n,k))