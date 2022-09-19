# 55_Kth_Largest_Element_in_an_Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/
import heapq
from typing import List


class Solution:
    # Solution0_1 - using sort
    def findKthLargest0_1(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]

    # Solution0_2 - using heapq
    def findKthLargest0_2(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)

        result = 0
        for _ in range(k):
            result = heapq.heappop(heap)

        return -result

    # Solution1 - using heapq
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        heap = list()

        for n in nums:
            heapq.heappush(heap, -n)

        for _ in range(1, k):
            heapq.heappop(heap)

        return -heapq.heappop(heap)

    # Solution2 - using heapify
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        print(nums)
        for _ in range(1, k):
            heapq.heappop(nums)
        return heapq.heappop(nums)

    """
    heapify를 사용하면 push를 사용하지 않고 힙을 만들 수 있다.
    """

    # Solution3 - using nlargest
    def findKthLargest3(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

    """
    nlargest는 가장 큰 값부터 n번째 큰 값까지 순서대로 리스트로 리턴됨
    """

    # Solution4 - using sort
    def findKthLargest4(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]

    """
    추가 삭제가 빈번할 때는 힙 정렬이 유용하지만, 입력값이 고정되어 있을 때는
    정렬 메서드를 사용하는 것으로 충분하다.
    """


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(Solution().findKthLargest3(nums, k))
