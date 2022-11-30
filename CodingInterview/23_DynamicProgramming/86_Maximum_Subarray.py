# 86_Maximum_Subarray
# https://leetcode.com/problems/maximum-subarray/
import sys
from typing import List


class Solution:
    # Solution0_1
    def maxSubArray0_1(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [- sys.maxsize] * (n + 1)
        for window_size in range(1, n + 1):
            print(dp)
            sub_sum = -sys.maxsize
            for idx in range(0, n - window_size + 1):
                sub_sum = max(sum(nums[idx:idx + window_size]), sub_sum)
            dp[window_size] = max(sub_sum, dp[window_size - 1])

        return dp[-1]

    """
    Time Limit Exceeded
    """

    # Solution0_2
    def maxSubArray0_2(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [- sys.maxsize] * (n + 1)
        dp[1] = max(nums)
        for window_size in range(2, n + 1):
            max_sub_sum = sum(nums[0:window_size])
            for idx in range(0, n - window_size + 1):
                if nums[idx + window_size - 1] >= 0:
                    max_sub_sum = max(sum(nums[idx:idx + window_size]), max_sub_sum)
            dp[window_size] = max(max_sub_sum, dp[window_size - 1])

        return dp[-1]

    """
    최적화 => 그래도 Time Limit Exceeded
    왜 Time Limit Exceed? 최적화를 했다고 해도 O(n^3) 의 시간복잡도
    """

    # Solution1 - memorization
    def maxSubArray1(self, nums: List[int]) -> int:
        sums = [nums[0]]
        for i in range(1, len(nums)):
            sums.append(nums[i] + (sums[i - 1] if sums[i - 1] > 0 else 0))

        return max(sums)

    """
    sums[i] 는 i 까지의 부분합의 최댓값. sums[i] 를 구할 때 현재 값인 nums[i] 와 이전 합인
    sums[i-1] 을 더하는데 sums[i-1] 이 음수라면 더할 필요가 없으므로, 그 때는 0 을 더한다.
    
    dp 의 설계가 잘못됨. Solution0 들은 index 기준으로 특정 window 까지 부분합의 최댓값을 구했었다.
    그렇게 생각하면 O(n^3)
    반면 Soltuion1 은 index 까지의 부분합의 최댓갑을 가진 list 인 sums 를 구하여
    max(sums) 를 return 한다. 
    Solution0_1 에서 0 이상인 값만 더한다는 접근은 좋았던것 같다.
    """

    # Solution2 - kadane algorithm
    def maxSubArray2(self, nums: List[int]) -> int:
        best_sum = -sys.maxsize
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)

        return best_sum

    """
    current_sum 은 num 까지의 부분합의 최댓값
    best_sum 은 current_sum 들의 최댓값
    Soltuion1 과 풀이 방법은 동일하다.
    """


# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums = [-2, -1]
print(Solution().maxSubArray0_2(nums))
