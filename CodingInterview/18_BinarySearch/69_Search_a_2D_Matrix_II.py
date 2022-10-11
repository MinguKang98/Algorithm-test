# 69_Search_a_2D_Matrix_II
# https://leetcode.com/problems/search-a-2d-matrix-ii/
from typing import List


class Solution:
    # solution0 - using binary search
    def searchMatrix0(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        for row in matrix:
            if row[0] <= target <= row[-1]:
                left, right = 0, n - 1
                while left <= right:
                    mid = left + (right - left) // 2
                    if row[mid] > target:
                        right = mid - 1
                    elif row[mid] < target:
                        left = mid + 1
                    else:
                        return True
            else:
                continue

        return False

    """
    target이 속하는 row 만 이진 검색
    """

    # solution1 -
    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        row = 0
        col = len(matrix[0]) - 1

        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -= 1
            elif target > matrix[row][col]:
                row += 1
        return False
    """
    첫 행의 맨 뒤 요소부터 탐색 시작
    현제 요소보다 타겟이 작으면 왼쪽으로 이동하고 타겟이 크면 아래로 이동한다.
    """

    # solution2 - pythonic
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in row for row in matrix)


matrix = [[1, 4, 7, 11, 15],
          [2, 5, 8, 12, 19],
          [3, 6, 9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]]
target = 5
print(Solution().searchMatrix2(matrix, target))
