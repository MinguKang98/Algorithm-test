# 9_3Sum
from typing import List

# solution0 - BruteForce
def threeSum0(nums: List[int]) -> List[List[int]]:
    N = len(nums)
    sum_list = []
    nums.sort()
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if nums[i] + nums[j] + nums[k] == 0:
                    temp_list = [nums[i], nums[j], nums[k]]
                    if temp_list in sum_list:
                        break
                    else:
                        sum_list.append(temp_list)
    return sum_list


"""
전체 시간복잡도 O(n^3)
Time LImit Exceeded
i,j,k의 범위 개선 필요
중복 제거 시도 했지만 시간이 많이 걸리는 연산 -> in 의 시간복잡도 O(n) 개선 필요
"""

# solution1 - BruteForce
def threeSum1(nums: List[int]) -> List[List[int]]:
    N = len(nums)
    sum_list = []
    nums.sort()

    for i in range(N - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, N - 1):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            for k in range(j + 1, N):
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    sum_list.append([nums[i], nums[j], nums[k]])
    return sum_list


"""
전체 시간복잡도 O(n^3)
여전히 Time LImit Exceeded
"""


# solution2 - Two Pointer
def threeSum2(nums: List[int]) -> List[List[int]]:
    N = len(nums)
    sum_list = []
    nums.sort()

    for i in range(N - 2):
        if i > 0 and nums[i] == nums[i - 1]:  # 중복 제거
            continue
        left, right = i + 1, N - 1
        sub_sum = -nums[i]

        while left < right:  # two pointer 연산
            if nums[left] + nums[right] > sub_sum:
                right -= 1
            elif nums[left] + nums[right] < sub_sum:
                left += 1
            else:
                sum_list.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:  # left의 중복 넘김
                    left += 1
                while left < right and nums[right] == nums[right - 1]:  # right의 중복 넘김
                    right -= 1
                # pointer 이동
                left += 1
                right -= 1

    return sum_list


"""
투포인터는 기존 O(n^2)의 시간복잡도를 O(n)으로 줄여줌
전체 시간복잡도는 O(n^2)
else 에서 left와 right의 중복 넘기는 부분 구현 실패
"""

nums = [-1, 0, 1, 2, -1, -4]
print(threeSum2(nums))
