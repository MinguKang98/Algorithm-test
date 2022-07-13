# 38_Reconstruct_Itinerary_332
from collections import defaultdict
from typing import List


class Solution:
    # Solution0 - using backtracking
    def findItinerary0_1(self, tickets: List[List[str]]) -> List[str]:
        result = []

        def dfs(start: str, candidates: List[int], path: List[int]):
            if len(path) == len(tickets):
                path.append(start)
                result.append(path[:])
                path.pop()
                return

            idx = -1
            for i in range(len(candidates)):
                if candidates[i][0] == start:
                    path.append(start)
                    idx = i
                    dest = candidates[idx][1]
                    dfs(dest, candidates[0:idx] + candidates[idx + 1 :], path)
                    path.pop()

        dfs("JFK", tickets, [])
        result.sort()
        return result[0]

    """
    Time Limit Exceeded -> dfs마다 for문 돌아 성능저하? list가 아닌 dic으로 구현한다면?
    """

    # Solution1 - using bfs recursive
    def findItinerary1(self, tickets: List[List[str]]) -> List[str]:
        result = []
        dict = defaultdict(list)
        for start, end in sorted(tickets):
            dict[start].append(end)

        def dfs(start: str):
            while dict[start]:
                dfs(dict[start].pop(0))
            result.append(start)

        dfs("JFK")
        return result[::-1]

    """
    연결이 끊긴 도시는 최종 연결지점들로 설정 -> 한붓그리기에 대한 이해 약간 필요;;
    dfs 중 연결이 끊긴다면 그 지점은 나중에 만날 예정 -> append함
    """

    # Solution2 - using bfs recursive with optimizing
    def findItinerary2(self, tickets: List[List[str]]) -> List[str]:
        result = []
        dict = defaultdict(list)
        for start, end in sorted(tickets, reverse=True):
            dict[start].append(end)

        def dfs(start: str):
            while dict[start]:
                dfs(dict[start].pop())
            result.append(start)

        dfs("JFK")
        return result[::-1]

    """
    dict을 reverse 시켜 pop(0)가 이닌 pop(1)을 할 수 있도록 함
    -> pop(0)는 O(n)인 반면 pop(1)은 O(1)이기 때문 
    """

    # Solution3 - using bfs iterative
    def findItinerary3(self, tickets: List[List[str]]) -> List[str]:
        dict = defaultdict(list)
        for start, end in sorted(tickets):
            dict[start].append(end)

        result = []
        stack = ["JFK"]

        while stack:
            while dict[stack[-1]]:
                stack.append(dict[stack[-1]].pop(0))
            result.append(stack.pop())
        return result[::-1]

    """
    stack과 queue를 이용한 dfs
    """


# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
tickets = [
    ["JFK", "SFO"],
    ["JFK", "ATL"],
    ["SFO", "ATL"],
    ["ATL", "JFK"],
    ["ATL", "SFO"],
]
# tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
print(Solution().findItinerary3(tickets))
