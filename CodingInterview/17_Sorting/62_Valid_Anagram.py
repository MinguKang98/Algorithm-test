# 62_Valid_Anagram
# https://leetcode.com/problems/valid-anagram/

class Solution:
    # Solution0 - using sort
    def isAnagram0(self, s: str, t: str) -> bool:
        return sorted(list(s)) == sorted(list(t))

    # Solution1 - using sort
    def isAnagram1(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    """
    str type도 sorted 가능. sort는 불가
    sorted 시 str 이 list 로 변경
    """

s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s, t))
