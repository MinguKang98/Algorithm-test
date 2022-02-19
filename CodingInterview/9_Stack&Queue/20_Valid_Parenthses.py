# 20_Valid_Parenthses


class Solution:
    # Solution0 - mine
    def isValid(self, s: str) -> bool:
        stack: list = []

        if len(s) % 2 == 1:
            return False

        for p in s:
            if p == "(" or p == "{" or p == "[":
                stack.append(p)
            else:
                if stack:
                    if p == ")" and stack[-1] == "(":
                        stack.pop()
                    elif p == "}" and stack[-1] == "{":
                        stack.pop()
                    elif p == "]" and stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
                else:
                    return False

        return len(stack) == 0

    # Solution1 - using dictionary
    def isValid(self, s: str) -> bool:
        stack: list = []
        table = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char not in table:  # 왼쪽 괄호의 경우
                stack.append(char)
            elif not stack or table[char] != stack.pop():  # 오른쪽 괄호의 경우
                return False

        return len(stack) == 0
