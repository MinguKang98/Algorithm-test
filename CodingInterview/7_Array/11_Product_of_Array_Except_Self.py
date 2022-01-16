# 11_Product_of_Array_Except_Self
from typing import List

# solution0
def productExceptSelf(nums: List[int]) -> List[int]:
    result = []
    N = len(nums)
    sub_list1 = [1]
    sub_list2 = [1]

    for i in range(N - 1):
        sub_list1.append(sub_list1[-1] * nums[i])

    reverse_nums = list(reversed(nums))
    for i in range(N - 1):
        sub_list2.append(sub_list2[-1] * reverse_nums[i])
    sub_list2.reverse()

    for i in range(N):
        result.append(sub_list1[i] * sub_list2[i])

    return result


# solution1
def productExceptSelf(nums: List[int]) -> List[int]:
    result = []
    p = 1

    # 왼쪽 곱셈
    for i in range(len(nums)):
        result.append(p)
        p = p * nums[i]

    # 오른쪽 곱셈
    p = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] = result[i] * p
        p = p * nums[i]

    return result


"""
자기 자신을 제외한 왼쪽 곱의 배열과 오른쪽 곱의 배열의 곱을 각각 구한 후 곱함
더 빠름
"""


nums = [1, 2, 3, 4]
print(productExceptSelf(nums))
