# 64_K_Closest_Points_to_Origin
# https://leetcode.com/problems/k-closest-points-to-origin/
import heapq
from typing import List


class Solution:
    # Solution0_1 - using built-in function
    def kClosest0_1(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
        return points[:k]

    # Solution0_2 - using priority queue
    def kClosest0_2(self, points: List[List[int]], k: int) -> List[List[int]]:
        queue = []
        for point in points:
            heapq.heappush(queue, (point[0] ** 2 + point[1] ** 2, point))

        result = []
        for _ in range(k):
            result.append(heapq.heappop(queue)[1])
        return result

    # Solution1 - using priority queue
    def kClosest1(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, (dist, x, y))

        result = []
        for _ in range(k):
            (dist, x, y) = heapq.heappop(heap)
            result.append((x, y))
        return result

    """
    정렬에 priority queue 를 사용할 수 있다
    """

points = [[3, 3], [5, -1], [-2, 4]]
k = 2
print(Solution().kClosest1(points, k))
