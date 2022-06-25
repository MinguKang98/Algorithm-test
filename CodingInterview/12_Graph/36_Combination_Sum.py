# 36_Combination_Sum
from typing import List


class Solution:
    # Solutino0 - using dfs
    def combinationSum0(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(elements: List[int], cdd: List[int]):
            if sum(elements) == target:
                result.append(elements[:])
                return

            for i in range(len(cdd)):
                elements.append(cdd[i])
                if sum(elements) <= target:
                    dfs(elements, cdd[i:])
                elements.pop()

        dfs([], candidates)
        return result

    # Solutino1 - using dfs
    def combinationSum1(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(
            csum: int, index: int, path: List[int]
        ):  # csum: 남은합, index: 현재 위치, path: 현재 경로
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return

            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return result


# candidates = [2, 3, 6, 7]
# target = 7
candidates = [2, 3, 5]
target = 8
print(Solution().combinationSum1(candidates, target))
