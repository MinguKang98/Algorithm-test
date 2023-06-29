# 4949_균형잡힌 세상
# Stack
import sys

# 처음 코드
def balance_world(str):
    stack = []
    for ch in str:
        if ch == "(":
            stack.append(ch)
        if ch == ")":
            if len(stack) == 0 or stack[-1] != "(":
                stack.append(ch)
            else:
                stack.pop(-1)
        if ch == "[":
            stack.append(ch)
        if ch == "]":
            if len(stack) == 0 or stack[-1] != "[":
                stack.append(ch)
            else:
                stack.pop(-1)

    if len(stack) == 0:
        print("yes")
    else:
        print("no")


# balance 한지만 판단하면 되느로 모든 수행을 할 필요는 없음
def balance_world2(str):
    stack = []
    for ch in str:
        if ch in "([":
            stack.append(ch)
        if ch == ")":
            if stack:
                if stack.pop() != "(":
                    return "no"
            else:
                return "no"
        if ch == "]":
            if stack:
                if stack.pop() != "[":
                    return "no"
            else:
                return "no"

    if stack:
        return "no"
    return "yes"


while True:
    str = sys.stdin.readline().rstrip()
    if str == ".":
        break
    print(balance_world2(str))
