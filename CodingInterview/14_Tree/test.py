# 49_Minimum_Height_Trees
# https://leetcode.com/problems/minimum-height-trees/
import collections
from typing import List


class Solution:

    # Solution 0 - using bfs
    def findMinHeightTrees0(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        def bfs(root: int):
            depth = -1
            visited = [root]
            queue = collections.deque([root])
            while queue:
                length = len(queue)
                for _ in range(length):
                    node = queue.pop()
                    for kkk in graph[node]:
                        if kkk not in visited:
                            queue.appendleft(kkk)
                            visited.append(kkk)
                depth += 1

            return depth

        result = collections.defaultdict(list)

        for i in range(n):
            result[bfs(i)].append(i)

        return result.get(min(result.keys()))

    """
    bfs로 각 노드 당 깊이를 계산한 후 그 중 최솟값을 가지는 노드를 return 했다.
    답은 맞으나 Time Limit Exceeded. 더 효율적인 방법을 찾아야 한다.
    """

    # Solution 1 - removing leaf node
    def findMinHeightTrees1(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        leaves = []
        for i in range(n):  # 리프 노드 추가
            if len(graph[i]) == 1:
                leaves.append(i)

        while len(graph) > 2:
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                graph.pop(leaf)

                if len(graph[neighbor]) == 1:  # 새로 생긴 리프 노드 추가
                    new_leaves.append(neighbor)
            leaves = new_leaves

        return list(graph.keys())

    """
    최소 깊이를 가지는 노드는 트리의 가장 가운데 있는 노드여야 한다. => 리프 노드를 계속 제거하여 남은 노드가 가장 가운데 있는 노드
    리프 노드 : graph 에서 value 한 개 
    """

    # Solution 1-1 - removing leaf node
    def findMinHeightTrees1_1(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        leaves = []
        for i in range(n):  # 리프 노드 추가
            if len(graph[i]) == 1:
                leaves.append(i)

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:  # 새로 생긴 리프 노드 추가
                    new_leaves.append(neighbor)
            leaves = new_leaves

        return leaves
    """
    로직은 같으나 코드가 약간 다름
    """

n = 6
edges = [[0, 1], [0, 2], [0, 3], [3, 4], [4, 5]]
print(Solution().findMinHeightTrees1(n, edges))
