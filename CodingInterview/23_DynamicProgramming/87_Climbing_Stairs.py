# 87_Climbing_Stairs
# https://leetcode.com/problems/climbing-stairs/
from collections import defaultdict


class Solution:
    # Solution0
    def climbStairs0(self, n: int) -> int:
        dp = [1, 1]
        if n == 1:
            return dp[n]

        for i in range(2, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])

        return dp[n]

    # Solution1 - using recursive
    def climbStairs1(self, n: int) -> int:
        if n == 1:
            return 1

        if n == 2:
            return 2

        return self.climbStairs1(n - 1) + self.climbStairs1(n - 2)

    """
    Time Limit Exceeded
    """

    # Solution2 - using memorization
    dp = defaultdict(int)

    def climbStairs2(self, n: int) -> int:
        if n <= 2:
            return n

        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.climbStairs2(n - 1) + self.climbStairs2(n - 2)
        return self.dp[n]


n = 3
print(Solution().climbStairs0(n))
