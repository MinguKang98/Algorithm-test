# 12_Best_Time_to_Buy_and_Sell_Stock
from typing import List
import sys

# solution0_1 - BruteForce
def maxProfit0_1(prices: List[int]) -> int:
    N = len(prices)
    result = 0

    for i in range(N - 1):
        for j in range(i + 1, N):
            temp_result = prices[j] - prices[i]
            if temp_result >= 0 and result < temp_result:
                result = temp_result
    if result > 0:
        return result
    else:
        return 0


"""
Time Limit Exceeded
전체 시간 복잡도 O(n^2)
"""
# solution0_2 - index min max
def maxProfit0_2(prices: List[int]) -> int:
    N = len(prices)
    min_value, max_value = 10001, -1
    for i in range(1, N):
        temp_diff = prices[i] - prices[i - 1]
        if temp_diff >= 0:
            max_value = max(max_value, prices[i])
        else:
            min_value = min(min_value, prices[i])

    result = max(0, max_value - min_value)
    return result


"""
오름차순 배열에서 Wrong Answer
"""


# solution1 - BruteForce
def maxProfit1(prices: List[int]) -> int:
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(max_price, prices[j] - price)

    return max_price


"""
Time Limit Exceeded
전체 시간 복잡도 O(n^2)
"""

# solution2 - min max
def maxProfit2(prices: List[int]) -> int:
    min_price = 10001
    # min_price = sys.maxsize
    result = 0

    for price in prices:
        min_price = min(price, min_price)
        result = max(result, price - min_price)

    return result


"""
max와 min 모두 구할 필요 없이 값들을 돌며 min 값만 최신화 후 계싼
전체 시간복잡도 O(n)
+ 10001보다 sys.maxsize 사용 시 더 빠름
"""

prices = [7, 1, 5, 3, 6, 4]
# prices = [7, 6, 4, 3, 1]
print(maxProfit2(prices))
