# 7_Two_Sum

from typing import List

# solution1 - BruteForce
def twoSum1(nums: List[int], target: int) -> List[int]:
    N = len(nums)
    for i in range(N):
        for j in range(i, N):
            if nums[i] + nums[j] == target:
                return [i, j]


"""
전체 시간복잡도 O(n^2)
"""


# solution2 - using in
def twoSum2(nums: List[int], target: int) -> List[int]:
    for idx, num in enumerate(nums):
        other_num = target - num

        if other_num in nums[idx + 1 :]:
            return [idx, nums[idx + 1 :].index(other_num) + idx + 1]


"""
전체 시간복잡도 O(n^2)
in의 시간복잡도가 O(n)이지만 연산이 가볍고 빠름
따라서 solution1 보다 빠름
"""

# solution3 - using key
def twoSum3(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    for idx, num in enumerate(nums):
        nums_map[num] = idx

    for idx, num in enumerate(nums):
        other_num = target - num
        if other_num in nums_map and idx != nums_map[other_num]:
            return [idx, nums_map[other_num]]


"""
전체 시간복잡도O(n)
dictionary는 해쉬테이블로 구현 -> 조회는 평균 O(1)
solution2 보다 빠름
"""

# solution4 - upgrade sol3
def twoSum4(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    for idx, num in enumerate(nums):
        other_num = target - num
        if other_num in nums_map:  # 있으면 반환
            return [nums_map[other_num], idx]
        nums_map[num] = idx  # 없으면 추가


"""
전체 시간복잡도O(n)
solution3 개선 - 루프 하나로 합침
sol3보다 빠른 속도 
"""

# solution5 - two pointer
def twoSum5(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1
    while not left == right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]


"""
전체 시간복잡도 O(n) 이지만
nums가 정렬된 상태가 아니므로 이방법으로 풀 수 없음
정렬 시켜도 index가 섞이므로 해결 불가
"""


nums = [2, 7, 11, 15]
target = 9
print(twoSum4(nums, target))
