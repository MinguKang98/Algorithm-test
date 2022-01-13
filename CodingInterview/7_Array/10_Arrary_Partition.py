# 10_Arrary_Partition
from typing import List

# solution0 & solution2 - even number
def arrayPairSum0(nums: List[int]) -> int:
    result = 0
    nums.sort()

    for i in range(len(nums)):
        if i % 2 == 0:
            result += nums[i]

    return result


"""
solution1보다 간결하고 약간 더 빠름
"""


# solution1 - ascending
def arrayPairSum1(nums: List[int]) -> int:
    result = 0
    sub_result = []
    nums.sort()

    for i in range(len(nums)):
        sub_result.append(nums[i])
        if len(sub_result) == 2:
            result += min(sub_result)
            sub_result = []

    return result


"""
시간 큰 차이 없음
+ 인덱스 접근(range(len(nums))과 직접 접근(range(nums)) 중 인덱스 접근이 더 빠름
"""

# solution3 - pythonic
def arrayPairSum3(nums: List[int]) -> int:
    return sum(sorted(nums)[::2])


"""
solution0(2)를 pythonic 하게 바꿈
가장 빠름
"""

nums = [1, 4, 3, 2]
print(arrayPairSum1(nums))
