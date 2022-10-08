# 65_Binary_Search
# https://leetcode.com/problems/binary-search/
import bisect
from typing import List


class Solution:
    # Solution1 - using recursive
    def search1(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left <= right:
                # mid = (left + right) // 2  => 오버플로의 위험이 있음
                mid = left + (right - left) // 2

                if nums[mid] < target:
                    return binary_search(mid + 1, right)
                elif nums[mid] > target:
                    return binary_search(left, mid - 1)
                else:
                    return mid
            else:
                return -1

        return binary_search(0, len(nums) - 1)

    # Solution2 - using iterative
    def search2(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            # mid = (left + right) // 2  => 오버플로의 위험이 있음
            mid = left + (right - left) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1

    # Solution3 - using binary search module
    def search3(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1

    # Solution4 - using index without binary search
    def search4(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1


nums = [5]
target = 5
print(Solution().search2(nums, target))
