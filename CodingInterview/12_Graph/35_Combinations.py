# 35_Combinations
from typing import List
import itertools


class Solution:
    # Solution0 - using dfs
    def combin0(self, n: int, k: int) -> List[List[int]]:
        def dfs(cur_list: List[int], res_list: List[int]):
            if len(cur_list) == k:
                result.append(cur_list)
                return

            for i in range(len(res_list)):
                dfs(cur_list + [res_list[i]], res_list[i + 1 :])

        result = []
        nums = list(range(1, n + 1))
        dfs([], nums[:])
        return result

    # Solution1 - using dfs
    def combine1(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(elements: List[int], start: int, k: int):
            if k == 0:
                result.append(elements[:])
                return

            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return result

    # Solution2 - using iterator tools
    def combine2(self, n: int, k: int) -> List[List[int]]:
        return list(map(list, itertools.combinations(range(1, n + 1), k)))


n = 4
k = 2
print(Solution().combine2(n, k))
