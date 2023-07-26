# 16953_A_B_Silver2
# https://www.acmicpc.net/problem/16953
from collections import deque

A, B = map(int, input().split())


def solution0():
    queue = deque()
    queue.appendleft((A, 0))

    result = 0
    while queue:
        cur_num, cur_cnt = queue.pop()
        if cur_num == B:
            result = cur_cnt
            break

        if cur_num > B:
            continue

        queue.appendleft((cur_num * 10 + 1, cur_cnt + 1))
        queue.appendleft((cur_num * 2, cur_cnt + 1))

    if not result:
        return -1
    return result + 1


"""
bfs 로 탐색하다 현재 값이 B 와 같아지면 break
만약 현재 값이 B보다 크면 해당 값에 대해서는 더 탐색 안해도 되므로 continue
마지막에 result 가 0인지 아닌지를 보고 값 반환
"""


def solution1(A, B):
    result = 1

    while True:
        if A == B:
            break
        elif A > B:
            result = -1
            break
        elif B % 10 == 1:
            B = B // 10
            result += 1
        elif B % 2 == 0:
            B = B // 2
            result += 1
        else:
            result = -1
            break

    return result


"""
A 에서 B 로 가는 계산이 아닌 B 에서 A 로 가는 계싼
1로 끝나면 1을 붙인 계산이므로 / 10
짝수면 2를 곱한 계산이므로 /2
A 가 더 크거면 계산 안되는 경우
나머지는 계산 안되는 경우
"""

print(solution1(A, B))
