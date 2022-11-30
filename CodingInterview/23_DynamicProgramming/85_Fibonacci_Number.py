# 85_Fibonacci_Number
# https://leetcode.com/problems/fibonacci-number/
from collections import defaultdict


class Solution:
    # Solution0 - dynamic programming
    def fib0(self, n: int) -> int:
        result = [0] * 31
        result[0] = 0
        result[1] = 1

        for i in range(2, n + 1):
            result[i] = result[i - 1] + result[i - 2]
        return result[n]

    # Solution1 - bruteforce
    def fib1(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib1(n - 1) + self.fib1(n - 2)

    # Solution2 - memorization
    dp = defaultdict(int)

    def fib2(self, n: int) -> int:
        if n <= 1:
            return n

        if self.dp[n]:
            return self.dp[n]

        self.dp[n] = self.fib2(n - 1) + self.fib2(n - 2)
        return self.dp(n)

    """
    Solution1 과 비슷하게 재귀로 풀지만, 계산한 값은 저장하여 필요할 때 바로
    return 한다.
    """

    # Solution3 - tabulation
    def fib3(self, n: int) -> int:
        dp = defaultdict(int)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    """
    재귀가 아닌 반복을 사용한다. 
    """

    # Solution4 - with two var
    def fib4(self, n: int) -> int:
        x, y = 0, 1
        for i in range(0, n):
            x, y = y, x + y
        return x
    """
    defaultdict 이나 list 가 아닌 변수 2개로 dp 가 가능하다.
    시간복잡도는 O(n) 으로 같으나 공간복잡도가 O(n) 에서 O(1) 로 줄어든다.
    """


n = 2
print(Solution().fib(n))
