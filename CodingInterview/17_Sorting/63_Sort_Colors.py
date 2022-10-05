# 63_Sort_Colors
# https://leetcode.com/problems/sort-colors/
from typing import List


class Solution:
    """
    Do not return anything, modify nums in-place instead.
    """

    # Solution 0-1 - using built-in function
    def sortColors0_1(self, nums: List[int]) -> None:
        nums.sort()

    # Solution 0-2 - using insertion sort
    def sortColors0_2(self, nums: List[int]) -> None:
        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

    # Solution 1 - using Dutch national flag problem
    def sortColors1(self, nums: List[int]) -> None:
        red, white, blue = 0, 0, len(nums)

        while white < blue:
            if nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] > 1:
                blue -= 1
                nums[white], nums[blue] = nums[blue], nums[white]
            else:
                white += 1

    """
    중간값을 기준으로 작은 값은 왼쪽으로 큰 값은 오른쪽으로 swap
    이때 red와 blue는 오른쪽과 왼쪽으로 움직이며 간격이 좁아짐
    O(n^2) 의 시간 복잡도를 가지는 insertion sort 와 달리 O(n) 의 시간 복잡도를 가진다
    세 부분으로 분할하는 문제의 경우 사용 가능한 알고리즘
    two pointer 와 비슷?
    """
