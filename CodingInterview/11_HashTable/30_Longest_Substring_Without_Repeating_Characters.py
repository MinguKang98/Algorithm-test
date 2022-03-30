# 30_Longest_Substring_Without_Repeating_Characters


class Solution:
    # Solution0 -
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = set()
        max_len = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] not in substr:
                    substr.add(s[j])
                else:
                    break
            max_len = max(max_len, len(substr))
            substr = set()

        return max_len

    """
    길이만 반환하면 되어 순서가 상관 없으므로 list 대신 set 사용
    list의 append보다 set의 add가 속도가 빠름
    """

    # Solution1 - using slicing window and two pointer
    def lengthOfLongestSubstring1(self, s: str) -> int:
        used = {}
        max_len = start = 0  # max_len으로 end확인 가능하므로 end 변수 따로 필요 없음
        for idx, char in enumerate(s):
            if char in used and start <= used[char]:
                # 이미 있는 글자면 start 새로 갱신 & 범위 내의 문자만 관리
                start = used[char] + 1  # 중복된 문자 다음부터 탐색 새로 시작
            else:  # 새로운 글자면 max_len 초기화
                max_len = max(max_len, idx - start + 1)

            used[char] = idx  # 현재 위치 갱신

        return max_len

    """
    Solution0보다 훨씬 빠름
    """


sol = Solution()
s = "abcabcbb"
print(sol.lengthOfLongestSubstring1(s))
