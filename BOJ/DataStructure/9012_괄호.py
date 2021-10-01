# 9012_괄호
# Stack
import sys


# list를 사용
def find_vps(pss: str):
    stack = []
    for ps in pss:
        if ps == "(":
            stack.append("(")
        else:
            # top of stack 이 ")" or empty 면 ")" 추가
            if len(stack) == 0 or stack[-1] == ")":
                stack.append(")")
            # top of stack 이 "(" 면 remove top
            else:
                stack.pop(-1)
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")


# index를 사용
def find_vps2(pss: str):
    stack = 0
    for ps in pss:
        if ps == "(":
            stack += 1
        else:
            stack -= 1
            if stack < 0:
                break
    if stack == 0:
        print("YES")
    else:
        print("NO")


N = int(input())
for i in range(N):
    find_vps2(sys.stdin.readline().strip())
