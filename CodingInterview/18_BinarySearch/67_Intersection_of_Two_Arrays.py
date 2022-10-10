# 67_Intersection_of_Two_Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/
import bisect
from typing import List, Set


class Solution:
    # Solution0_1 - using built-in function "in"
    def intersection0_1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()
        for num in nums1:
            if num in nums2:
                result.add(num)
        return list(result)

    # Solution0_2 - using binary search
    def intersection0_2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()
        nums2.sort()
        for target in nums1:
            left, right = 0, len(nums2) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums2[mid] > target:
                    right = mid - 1
                elif nums2[mid] < target:
                    left = mid + 1
                else:
                    result.add(nums2[mid])
                    break

        return result

    """
    1. 한 배열을 기준으로 다른 배열을 탐색한다.
    2. 탐색방법 -> bruteforce, binary search, in function 등이 있다.
    탐색방법에 따라 시간복잡도가 달라진다.
    """

    # Solution1 - using bruteforce
    def intersection1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()
        for n1 in nums1:
            for n2 in nums2:
                if n1 == n2:
                    result.add(n1)

        return result

    """
    브루트 포스는 O(n^2) 의 시간복잡도를 가진다.        
    """

    # Solution2 - using bruteforce
    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()
        nums2.sort()
        for n1 in nums1:
            i2 = bisect.bisect_left(nums2, n1)
            if len(nums2) > 0 and i2 < len(nums2) and n1 == nums2[i2]:
                result.add(n1)

        return result

    """
    nums1 순회 시 O(n), nums2 를 이진 검색 하며 O(logn), 총 O(nlogn) 의 시간 복잡도를 가진다.
    """

    # Solution3 - using two pointer
    def intersection3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()
        nums1.sort()
        nums2.sort()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                result.add(nums1[i])
                i += 1
                j += 1

        return result

    """
    투 포인터를 사용하면 O(n) 의 시간복잡도를 가진다.
    한 배열의 시작과 끝에서만 투 포인터를 쓸 수 있는 것이 아니라 두 배열을 비교할 때도 사용 가능하다.
    """
