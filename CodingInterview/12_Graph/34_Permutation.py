# 34_Permutation
from typing import List
from itertools import permutations


class Solution:
    # Solution 0-1 - using dfs
    def permute0_1(self, nums: List[int]) -> List[List[int]]:
        def dfs(ans: List[int], rest_nums: List[int]):
            if len(rest_nums) == 0:
                result.append(ans)

            for i in range(len(rest_nums)):
                dfs(ans + [rest_nums[i]], rest_nums[0:i] + rest_nums[i + 1 :])

        result = []
        dfs([], nums)
        return result

    # Solution 0-2 - using iterator tools
    def permute0_2(self, nums: List[int]) -> List[List[int]]:
        return list(map(list, permutations(nums)))

    # Solutino 1 - using using dfs
    def permute1(self, nums: List[int]) -> List[List[int]]:
        result = []
        prev_elements = []

        def dfs(elements: List[int]):
            if len(elements) == 0:
                result.append(prev_elements[:])

            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return result


nums = [1, 2, 3]
print(Solution().permute1(nums))
