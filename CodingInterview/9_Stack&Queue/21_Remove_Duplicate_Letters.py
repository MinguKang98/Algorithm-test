# 21_Remove_Duplicate_Letters
import collections
from re import S
from turtle import st


class Solution:
    # Solution0 - mine
    def removeDuplicateLetters0(self, s: str) -> str:
        substr = []
        for c in s:
            if c not in substr:
                substr.append(c)
            else:
                if substr[0] == c:
                    substr.pop(0)
                    substr.append(c)
        return "".join(substr)

    """
    문제 이해 부족 -> Wrong Answer
    """

    # Solution1 - Recursion 사용
    def removeDuplicateLetters1(self, s: str) -> str:

        for char in sorted(set(s)):  # 적절한 char 선택..
            substr = s[s.index(char) :]  # char로 시작하는 substr indexing
            if set(s) == set(substr):  # substr의 알파벳들과 s의 알파벳이 같으면 재귀 시행
                return char + self.removeDuplicateLetters1(
                    substr.replace(char, "")
                )  # char 제거한 substr을 재귀
        return ""  # s가 ""라면 "" return

    # Solution2 - Stack 사용
    def removeDuplicateLetters2(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []
        # char의 개수파악 위해 counter 사용
        # 처리된 문자 확인 위해 set 사용(중복 허용X)

        for char in s:  # 첫글자부터 순환
            counter[char] -= 1
            if char in seen:  # 봤던 글자라면 pass
                continue
            while (
                stack and stack[-1] > char and counter[stack[-1]] > 0
            ):  # 뒤에 붙일 문자가 있다면 스택 제거
                # 스택 not empty & stack의 top이 char보다 후순위 & stack의 top 여분 존재
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return "".join(stack)

        """
        Solution1보다 조금 더 빠름
        """

    # Solution3 - list 사용
    def removeDuplicateLetters3(self, s: str) -> str:
        counter, list = collections.Counter(s), []

        for char in s:
            counter[char] -= 1
            if char in list:  # list이므로 set사용하지 않고 확인 가능
                continue
            while list and list[-1] > char and counter[list[-1]] > 0:
                list.pop()
            list.append(char)

        return "".join(list)
