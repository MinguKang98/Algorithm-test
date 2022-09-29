# 61_Largest_Number
# https://leetcode.com/problems/largest-number/
from typing import List


class Solution:
    # Solution0 - using insertion sort
    def largestNumber0(self, nums: List[int]) -> str:

        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                if str(nums[j]) + str(nums[j + 1]) < str(nums[j + 1]) + str(nums[j]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return str(int(''.join(str(n) for n in nums)))

    """
    두 수의 조합 중 큰 수를 만드는 방법을 판단 
    처음엔 0 ~ i 까지 합쳐서 판단하려고 함 -> 비교하는 대상 중에 큰거만 골라도 됨
    0이 앞으로 오는 경우 0을 그대로 씀 : return ''.join() => return str(int(''.join())) 으로 변경 
    """

    # Solution1 - using insertion sort
    @staticmethod
    def to_swap(n1: int, n2: int) -> bool:
        return str(n1) + str(n2) < str(n2) + str(n1)

    def largestNumber1(self, nums: List[int]) -> str:
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
            i += 1

        return str(int(''.join(map(str, nums))))

    """
    비교하는 부분을 to_swap 메서드로 생성
    Solution0는 for-loop 인 반면 Solution1 은 while-loop
    map 사용하여 join
    """


nums = [3, 30, 34, 5, 9]
print(Solution().largestNumber0(nums))
