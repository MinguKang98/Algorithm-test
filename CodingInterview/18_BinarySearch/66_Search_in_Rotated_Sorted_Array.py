# 66_Search_in_Rotated_Sorted_Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import List


class Solution:
    # Solution 0
    def search0(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # 가장 작은 값의 index => pivot 찾음
        pivot = 0
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                pivot = i
                break

        # 이진 탐색으로 target의 index 찾음
        new_nums = nums[pivot:] + nums[:pivot]
        index = -1
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if new_nums[mid] < target:
                left = mid + 1
            elif new_nums[mid] > target:
                right = mid - 1
            else:
                index = mid
                break

        return (index + pivot) % n if index != -1 else -1

    """
    pivot 찾고 index 찾은 후 그 둘의 합을 len(nums) 로 나눈 나머지를 return
    나머지를 return 하는 이유는 return 하는 값이 len(nums) 보다 크면 안되기 때문
    이때 index == -1 이면 return -1
    """

    # Solution 1
    def search1(self, nums: List[int], target: int) -> int:

        if not nums:
            return -1

        # pivot 찾기
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left
        # pivot = nums.index(min(nums)) 로 축약 가능

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_pivot = (mid + pivot) % len(nums)

            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot
        return -1


nums = [3, 1]
target = 3
print(Solution().search0(nums, target))
