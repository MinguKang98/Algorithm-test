# 1_correct_parentheses
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution0(s):
    stack = []
    for p in s:
        if p == '(':
            stack.append(p)
        else:
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                return False

    return len(stack) == 0


"""
스택 사용
"""


def solution1(s):
    pair = 0
    for p in s:
        if pair < 0:
            break
        if p == "(":
            pair += 1
        else:
            pair -= 1

    return pair == 0


"""
숫자로 카운트
"""

s = ")()("
print(solution0(s))
