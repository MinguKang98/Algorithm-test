# 75_Sliding_Window_Maximum
# https://leetcode.com/problems/sliding-window-maximum/
from collections import deque
import sys
from typing import List


class Solution:
    # Solution 0_1 - using bruteforce
    def maxSlidingWindow0_1(self, nums: List[int], k: int) -> List[int]:
        result = []
        for i in range(len(nums) - k + 1):
            window = nums[i:i + k]
            result.append(max(window))

        return result

    """
    Time Limit Exceeded
    슬라이싱 윈도우로 인한 과도한 리스트 생성이 원인??
    """

    # Solution 0_2 - using queue
    def maxSlidingWindow0_2(self, nums: List[int], k: int) -> List[int]:
        result = []
        queue = deque()
        for i in range(k - 1):
            queue.append(nums[i])

        cur_max = -sys.maxsize
        for i in range(k - 1, len(nums)):
            queue.append(nums[i])
            if nums[i] > cur_max:
                cur_max = max(queue)
            result.append(cur_max)
            if cur_max == queue.popleft():
                cur_max = -sys.maxsize

        return result

    """
    Time Limit Exceeded
    max 사용 때문에? 어떻게 최적화? => 새로 들어온 값과 기존 max 값 비교
    => 그래도 Time LImit Exceeded
    """

    # Solution 1 - using queue
    def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
        current_max = float('-inf')
        window = deque()
        results = []

        for i, num in enumerate(nums):
            window.append(num)
            if i < k - 1:
                continue  # window size - 1 만큼 초기에 append

            if current_max == float('-inf'):
                current_max = max(window)
            elif num > current_max:
                current_max = num

            results.append(current_max) # window 에서의 최댓값 append

            if current_max == window.popleft():  # 최대값이 pop 되면 current_max 초기화
                current_max = float('-inf')

        return results

    """
    current_max == float('-inf') 이면 다시 최댓값 구해야하므로 max(window) 로 current_max 초기화
    nums > current_max 이면 nums 가 새로운 최댓값이므로 nums 로 current_max 초기화
    나머지 경우는 current_max 유지
    
    테스트케이스 변경으로 시간초과...
    """

    # Solution 2 - using queue
    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        window = deque()  # 인덱스가 담긴다. window[0] 가 current_max, 내림차순 정렬
        result = []
        for i, num in enumerate(nums):
            while window and nums[window[-1]] < num:    # num 이 nums[window[-1]] 보다 크다면 pop
                window.pop()

            window.append(i)  # 현재 인덱스 window 에 추가
            if window[0] <= i - k:  # window[0] 가 window 밖이면 popleft
                window.popleft()
            print(window, [nums[i] for i in window])
            if i >= k - 1:  # 첫 window 부터 nums(window[0]) append
                result.append(nums[window[0]])
        return result

    """
    window 의 첫 element 가 항상 curremtn_max 가 되도록 유지
    nums 순회 시 현재 num 이 window 의 가장 작은 element 보다 크다면 window.pop
    i >= k-1 이라면 항상 result.append
    
    window[0] 이 항상 current_max 이고 추가할 num 이 nums[window[-1]] 보다 크다면 window.pop
    하여 성능을 향상시킨 것으로 보임 
    """


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
# nums = [1]
# k = 1
print(Solution().maxSlidingWindow2(nums, k))
