# 78_Best_Time_to_Buy_and_Sell_Stock_II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
from typing import List


class Solution:
    # Solution0 - greedy
    def maxProfit0(self, prices: List[int]) -> int:
        benefit = 0
        for idx in range(1, len(prices)):
            diff = prices[idx] - prices[idx - 1]
            if diff > 0:
                benefit += diff

        return benefit

    """
    기울기가 양수인 것만 더하기 => 앞뒤 차가 양수면 항상 더한다
    """

    # Solution1 - greedy
    def maxProfit1(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                result += prices[i + 1] - prices[i]
        return result

    # Solution2 - pythonic
    def maxProfit2(self, prices: List[int]) -> int:
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))


prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices))
