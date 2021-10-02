# 1874_스택 수열
# Stack
import sys
from typing import List


def stack_seq() -> str:
    number = list(range(1, N + 1))
    op_list = []
    stack = []
    idx = 0
    for i in range(N):
        while len(stack) == 0 or stack[-1] != num_list[i]:
            if idx == N and stack:
                return "NO"
            stack.append(number[idx])
            op_list.append("+")
            idx += 1
        stack.pop(-1)
        op_list.append("-")
    return "\n".join(op_list)


def stack_seq2() -> str:
    op_list, stack, cnt = [], [], 1
    for num in num_list:
        while cnt <= num:
            stack.append(cnt)
            op_list.append("+")
            cnt += 1
        if stack.pop() == num:
            op_list.append("-")
        else:
            return "NO"
    return "\n".join(op_list)


N = int(sys.stdin.readline().rstrip())
num_list = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
print(stack_seq2())
