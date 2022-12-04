# 88_House_Robber
# https://leetcode.com/problems/house-robber/
from typing import List
from collections import OrderedDict


class Solution:
    # Solution0 - using tabulation
    def rob0(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        sums = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)):
            sums.append(max(sums[i - 1], nums[i] + sums[i - 2]))
        return sums[-1]

    """
    sums[i] : i 까지의 최댓값
    """

    # Solution1 - using recursive bruteforce
    def rob1(self, nums: List[int]) -> int:
        def _rob(i: int) -> int:
            if i < 0:
                return 0
            return max(_rob(i - 1), _rob(i - 2) + nums[i])

        return _rob(len(nums) - 1)

    """
    Time Limit Exceeded
    """

    # Solution2 - using tabulation
    def rob2(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) <= 2:
            return max(nums)

        dp = OrderedDict()
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return dp.popitem()[1]

    """
    OrderedDict 은 딕셔너리 입력 순서 유지. python 3.7 이상부터는 dictionary 입력순서가 유지된다. 이전은 유지 X
    """


nums = [1, 2, 3, 1]
print(Solution().rob2(nums))
