# 59_Merge_Intervals
# https://leetcode.com/problems/merge-intervals/
from typing import List


class Solution:
    # Solution0
    def merge0(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        result = [intervals[0]]
        for i in range(1, len(intervals)):
            if result[-1][1] >= intervals[i][0]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])
        return result

    """
    intervals 정렬 후, result[-1] 과 intervals[i] 비교. 정렬된 상태이므로 두 값만 비교하면 됨.
    겹치면 result[-1] 값 수정, 안 겹치면 result.append(intervals[i])
    """

    # Solution1
    def merge1(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        for i in sorted(intervals, key=lambda x: x[0]):
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged += i,    # = merged += [i]
        return merged
    
    """
    방법 거의 유사. 정렬 시 key 값을 정해줌
    """