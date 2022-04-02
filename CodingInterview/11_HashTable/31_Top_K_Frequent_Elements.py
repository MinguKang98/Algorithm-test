# 31_Top_K_Frequent_Elements
import heapq
from typing import List
from collections import Counter


class Solution:
    # Solution0 - using Counter
    def topKFrequent0(self, nums: List[int], k: int) -> List[int]:
        result = []
        counts = Counter(nums)

        return [count[0] for count in counts.most_common(k)]

    # Solution1 - using counter and heapq
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        freqs_heap = []
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))
        # heqpq는 min-heap을 지원함 -> 큰 값을 먼저 꺼내야하므로 빈도수에 -를 붙임
        # heapq 배열을 위한 배교값인 빈도수와 숫자로 tuple 생성 -> (빈도수, 숫자)

        topk = []
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])
        return topk

    # Solution2 - pythonic style
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*Counter(nums).most_common(k)))[0]


sol = Solution()
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(sol.topKFrequent2(nums, k))
