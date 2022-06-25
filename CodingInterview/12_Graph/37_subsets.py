# 37_subsets
from typing import List


class Solution:
    # Solution0 - using dfs
    def subsets0(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(path: List[int], candidates: List[int]):
            result.append(path[:])  # append(path)를 하면 같은 변수를 계속 추가하므로 path[:]사용

            for i in range(len(candidates)):
                path.append(candidates[i])
                dfs(path, candidates[i + 1 :])
                path.pop()

        dfs([], nums)
        return result

    # Solution1 - using dfs
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(index: int, path: List[int]):
            result.append(path)  # dfs에서 받는 path+[nums[i]]는 새로운 변수이므로 path로 append 가능

            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return result


nums = [1, 2, 3]
print(Solution().subsets0(nums))
