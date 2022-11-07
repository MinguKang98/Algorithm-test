# 76_Minimum_Window_Substring
# https://leetcode.com/problems/minimum-window-substring/
from collections import deque, Counter
from typing import Deque, List


class Solution:
    # Solution0 - using BruteForce
    def minWindow0(self, s: str, t: str) -> str:
        def t_in_window(t: str, window: Deque):
            check = window.copy()
            for char in t:
                if char not in check:
                    return False
                check.remove(char)
            return True

        if len(t) > len(s):
            return ''

        for window_size in range(len(t), len(s) + 1):
            window = deque()
            for idx in range(window_size - 1):
                window.append(s[idx])

            for idx in range(window_size - 1, len(s)):
                window.append(s[idx])
                if t_in_window(t, window):
                    return ''.join(window)
                window.popleft()
        return ''

    """
    Time Limit Exceeded
    성능 개선 어디서??    
    """

    # Solution1 - using BruteForce
    def minWindow1(self, s: str, t: str) -> str:
        def contains(s_substr_lst: List, t_list: List):
            for t_elem in t_list:
                if t_elem in s_substr_lst:
                    s_substr_lst.remove(t_elem)
                else:
                    return False
            return True

        if not s or not t:
            return ''

        window_size = len(t)

        for size in range(window_size, len(s) + 1):
            for left in range(len(s) - size + 1):
                s_substr = s[left:left + size]
                if contains(list(s_substr), list(t)):
                    return s_substr
        return ''

    """
    Time Limit Exceeded
    Solution0 와 코드 유사
    """

    # Solution2 - using sliding window & two pointer
    def minWindow2(self, s: str, t: str) -> str:
        need = Counter(t)  # 문자별 필요한 갯수
        missing = len(t)  # 필요한 문자의 전체 갯수
        left = start = end = 0

        for right, char in enumerate(s, 1):
            missing -= need[char] > 0  # t 안에 char 이 있다면 missing 1 감소
            need[char] -= 1

            # window 에 t의 모든 문자가 포함된 상태 => left 이동 가능하면 이동
            if missing == 0:
                # left 에 불필요한 문자 존재
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                # start, end 갱신
                if not end or (right - left) <= (end - start):
                    start, end = left, right

                # 다른 경우도 있는지 확인 위한 초기화 left 한칸 밀기
                need[s[left]] += 1
                missing += 1
                left += 1

        return s[start:end]

    """
    left, right : 탐색 위한 포인터
    start, end : 정답 위한 포인터
    
    counter 를 사용해 in 을 통해 문자로 찾지 않고 보다 빠르게 속하는지 판단 가능
    missing == 0 인 right pointer 와 need[s[left]] == 0 인 left pointer 가 정답
    그 중 가장 차이가 작은 left , right 가 start, end 가 됨
    """

    # Solution3 - using Counter
    def minWindow3(self, s: str, t: str) -> str:
        t_count = Counter(t)
        current_count = Counter()  # missing 대신 사용

        start = float('-inf')
        end = float('inf')

        left = 0
        for right, char in enumerate(s, 1):
            current_count[char] += 1

            # AND 연산의 결과가 같다면 window 에 t의 모든 문자가 포함된 상태
            while current_count & t_count == t_count:
                if (right - left) < (end - start):
                    start, end = left, right
                current_count[s[left]] -= 1
                left += 1

        return s[start:end] if end - start <= len(s) else ''

    """
    코드가 간편해지지만 Counter 의 AND 연산이 무거운 연산이므로 시간이 오래걸림
    """


s = "ADOBECODEBANC"
t = "ABC"
print(Solution().minWindow3(s, t))
