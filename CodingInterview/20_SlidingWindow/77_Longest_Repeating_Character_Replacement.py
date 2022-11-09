# 77_Longest_Repeating_Character_Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/
from collections import Counter


class Solution:
    # Solutino0 -
    def characterReplacement0(self, s: str, k: int) -> int:
        result = 0
        count = k

        left = 0
        for right, char in enumerate(s, 1):
            if count != 0 and char != s[left]:
                count -= 1

            if count == 0 and (right == len(s) or s[left] != s[right]):
                size = right - left
                result = max(result, size)
                count = k
                left = right - (size - k - 1)

        return result

    """
    무엇을 몇 번 변경??
    순회 하면서 left 와 right 문자 다르면  left 로 변경 시도

    오답 
    right 를 순회하고 특정 상황에서 left 를 이동시키는 생각은 맞았지만 전체적인 풀이가 틀림
    """

    # Solution1 -
    def characterReplacement1(self, s: str, k: int) -> int:
        left = right = 0
        counts = Counter()
        max_len = 0
        for right in range(1, len(s) + 1):
            counts[s[right - 1]] += 1
            max_char_n = counts.most_common(1)[0][1]

            if right - left - max_char_n > k:  # 연속되지 않고 다른 문자가 섞임
                counts[s[left]] -= 1
                left += 1

            max_len = max(right - left, max_len)
        return max_len

    """
    right 와 left 의 차에서 가장 빈도가 높은 문자의 수를 뺀 값 == k 라면 연속으로 반복된 문자열
    그중 가장 큰 값이 result 가 됨
    만약 right - left - max_char_n > k 라면 left 를 이동시킴
    """

    # Solution2 -
    def characterReplacement1(self, s: str, k: int) -> int:
        left = right = 0
        counts = Counter()
        max_len = 0
        for right in range(1, len(s) + 1):
            counts[s[right - 1]] += 1
            max_char_n = counts.most_common(1)[0][1]

            if right - left - max_char_n > k:  # 연속되지 않고 다른 문자가 섞임
                counts[s[left]] -= 1
                left += 1

        return right - left

    """
    max_len 구하는 부분 생략 가능
    한번 최댓값이 되면 right 가 1 이동할 때마다 left 도 1 이동
    """


s = "AAABBC"
k = 2
print(Solution().characterReplacement1(s, k))
