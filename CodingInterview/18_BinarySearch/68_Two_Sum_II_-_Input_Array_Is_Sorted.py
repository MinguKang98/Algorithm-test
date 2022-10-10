# 68_Two_Sum_II_-_Input_Array_Is_Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
import bisect
from typing import List


class Solution:
    # Solution0 - using two pointer (Solution1 와 풀이 동일)
    def twoSum0(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                return [left + 1, right + 1]

    """
    투 포인터는 O(n) 의 시간복잡도를 가진다.
    """

    # Solution2 - using binary search
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        for idx, num in enumerate(numbers):
            left, right = idx + 1, len(numbers) - 1
            expected = target - num
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] > expected:
                    right = mid - 1
                elif numbers[mid] < expected:
                    left = mid + 1
                else:
                    return idx + 1, mid + 1

    """
    이진 검색은 O(nlogn) 의 시간복잡도를 가진다.
    현재 값을 기준으로 나머지 값이 있는지 확인(ex. 합이 10, 현재 값이 3 이라면 7이 존재하는지 확인)
    """

    # Solution3 - using bisect + slicing 1
    def twoSum3(self, numbers: List[int], target: int) -> List[int]:
        for idx, num in enumerate(numbers):
            expected = target - num
            i = bisect.bisect_left(numbers[idx + 1:], expected)
            if i < len(numbers[idx + 1:]) and numbers[i + idx + 1] == expected:
                return idx + 1, i + idx + 2

    """
    bisect 모듈을 사용했지만 슬라이싱의 남용으로 시간이 오래 걸림
    슬라이싱은 참조가 아닌 매번 새로운 객체를 생성하기 때문이다.
    """

    # Solution4 - using bisect + slicing 2
    def twoSum4(self, numbers: List[int], target: int) -> List[int]:
        for idx, num in enumerate(numbers):
            expected = target - num
            nums = numbers[idx + 1:]
            i = bisect.bisect_left(nums, expected)
            if i < len(nums) and numbers[i + idx + 1] == expected:
                return idx + 1, i + idx + 2

    """
    슬라이싱을 최소화하여 성능 개선
    """

    # Solution5 - using bisect + slicing 3
    def twoSum5(self, numbers: List[int], target: int) -> List[int]:
        for idx, num in enumerate(numbers):
            expected = target - num
            i = bisect.bisect_left(numbers, expected, idx + 1)
            if i < len(numbers) and numbers[i] == expected:
                return idx + 1, i + 1

    """
    bisect.bisect_left(a, x, lo=0, hi=len(a))
    bisect_left 메서드에는 왼쪽 범위를 제한하는 파라미터 lo가 존재하므로 lo에 idx+1 을 넣어준다.
    이진 검색이지만 투 포인터와 비슷한 성능을 가진다.
    """


print(Solution().twoSum2([2, 7, 11, 15], 9))
