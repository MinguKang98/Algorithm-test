# 8_Trapping_Rain_Water

from typing import List

# solution1 - two pointer
def trap1(height: List[int]) -> int:
    total = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:  # left와 right가 같아질 때까지 반복 -> 전체의 max에서 만남
        left_max, right_max = max(left_max, height[left]), max(
            right_max, height[right]
        )  # 현재와 이전 최댓값중 최댓값 선택

        if left_max < right_max:
            total += left_max - height[left]
            left += 1
        else:
            total += right_max - height[right]
            right -= 1

    return total


"""
전체 시간복잡도 O(n)
"""

# solution2 - stack
def trap2(height: List[int]) -> int:
    stack = []
    total = 0

    for i in range(len(height)):  # index 순회
        while stack and height[i] > height[stack[-1]]:  # 변곡점(현재 높이가 이전 높이보다 높을때) 만나면
            top = stack.pop()
            if not len(stack):  # stack 비어있으면 break
                break

            distance = i - stack[-1] - 1  # 가로 길이
            water = min(height[i], height[stack[-1]]) - height[top]  # 세로 길이
            total += distance * water

        stack.append(i)

    return total


"""
전체 시간복잡도 O(n)
어려움
더 빠름
"""

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap1(height))
