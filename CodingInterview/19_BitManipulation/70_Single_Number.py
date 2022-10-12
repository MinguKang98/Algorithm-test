# 70_Single_Number
# https://leetcode.com/problems/single-number/
import collections
from typing import List


class Solution:
    # Solution0 - using counter
    def singleNumber0(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        result = min(counter, key=counter.get)
        return result

    """
    counter 사용하여 풀이
    min은 기본적으로 key 값을 기준으로 연산하므로 min 의 key 를 counter.get 으로 주어
    counter 의 value가 가장 작은 key 값을 찾도록 함
    result = value 값이 가장 작은 key
    """

    # Solution1 - using xor
    def singleNumber1(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result

    """
    xor 은 입력값이 다르면 true 같으면 false 이다
    두 번 등장하면 0으로 초기화 되고 한번만 등장하면 그 값을 보존한다.
    따라서 nums 에 대해 모두 xor 연산을 하면 single number 만 남게 된다.
    """


nums = [4, 1, 2, 1, 2]
print(Solution().singleNumber0(nums))
