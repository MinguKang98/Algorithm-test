# 83_Majority_Element
# https://leetcode.com/problems/majority-element/
from collections import defaultdict
from typing import List


class Solution:
    # Solution0 - devide and conquer
    def majorityElement0(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            N = len(nums) // 2
            element1 = self.majorityElement0(nums[:N])
            element2 = self.majorityElement0(nums[N:])
            return element1 if nums.count(element1) > N else element2

    """
    element 하나일 때까지 divide
    합칠 때 element1, element2 중 element1 의 갯수가 N 초과(절반 이상) 이면 element1 을, 아니라면 element2 를 return
    문제에서 가장 majority element 는 절반 이상이락 보장했기 때문이다.
    """

    # Solution1 - bruteforce
    def majorityElement1(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) > len(nums) // 2:
                return num

    """
    Time Limit Exceeded
    """

    # Solution2 - dynamic programming
    def majorityElement2(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for num in nums:
            if counts[num] == 0:
                counts[num] = nums.count(num)

            if counts[num] > len(nums) // 2:
                return num

    """
    counts 를 사용해 한번 계산한 값은 저하는 memeorizaiton 을 사용하므로 비교적 빠른 속도로 계산된다.
    """

    # Solution3 - devide and conquer
    def majorityElement3(self, nums: List[int]) -> int:
        if not nums:  # None 처리
            return None

        if len(nums) == 1:  # 분할 끊기
            return nums[0]
        else:
            # 분할
            half = len(nums) // 2
            a = self.majorityElement3(nums[:half])
            b = self.majorityElement3(nums[half:])

            # 정복
            return [b, a][nums.count(a) > half]
            # a 가 절반보다 많으면 1 이므로 return a, 아니면 0 이므로 return b

    """
    solution0 과 같은 풀이. 재귀의 특성 상 속도가 다소 느리다
    """

    # Solution4 - pythonic
    def majorityElement4(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]


# nums = [3, 2, 3]
nums = [6, 5, 5]
# nums = [2, 2, 1, 1, 1, 2, 2]
print(Solution().majorityElement0(nums))
