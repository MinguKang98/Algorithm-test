# 82_Assign_Cookies
# https://leetcode.com/problems/assign-cookies/
import bisect
from typing import List


class Solution:
    # Solution0 - using greedy
    def findContentChildren0(self, g: List[int], s: List[int]) -> int:
        s.sort()
        count = 0
        for greed_factor in g:
            for i in range(len(s)):
                if s[i] >= greed_factor:
                    count += 1
                    s[i] = 0
                    break

        return count

    """
    정렬 조건이 없어 정렬 휴 greedy
    O(n^2) : 매우 느림, 성공할 때도 있고 Time Limit Exceeded 날 때도 있음
    """

    # Solution1 - using greedy
    def findContentChildren1(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        child_i, cookie_j = 0, 0
        while child_i < len(g) and cookie_j < len(s):
            if g[child_i] <= s[cookie_j]:
                child_i += 1
            cookie_j += 1

        return child_i

    """
    비슷한 풀이지만 while 문을 잘 구성하니 훨씬 좋은 성능을 가지게 된다.
    """

    # Solution2 - using binary search
    def findContentChildren1(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        result = 0
        for i in s:
            index = bisect.bisect_right(g, i)
            if index > result:
                result += 1

        return result

    """
    이진검색으로 찾아낸 인덱스가 현재 쿠키를 나눠준 아이들보다 크다면 더 줄수 있다는 뜻
    """


# g = [1, 2, 3]
g = [1, 2]
# s = [1, 1]
s = [1, 2, 3]
print(Solution().findContentChildren1(g, s))
