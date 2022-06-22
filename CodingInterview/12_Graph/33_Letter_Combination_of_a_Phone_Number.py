# 33_Letter_Combination_of_a_Phone_Number
from typing import List


class Solution:
    # Solution0 - using BackTracking
    def letterCombinations0(self, digits: str) -> List[str]:
        num_dict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def letterCombi(letter: str, digits: str):
            if len(digits) == 0:
                result.append(letter)
                return

            first = digits[0]
            for alphabet in num_dict[first]:
                letterCombi(letter + alphabet, digits[1:])

        result = []
        if len(digits) == 0:
            return result

        first = digits[0]
        for letter in num_dict[first]:
            letterCombi(letter, digits[1:])
        return result

    # Solution1 - using BackTracking
    def letterCombinations1(self, digits: str) -> List[str]:
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return

            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)

        if not digits:
            return []

        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = []
        dfs(0, "")
        return result


digits = "23"
print(Solution().letterCombinations1(digits))
