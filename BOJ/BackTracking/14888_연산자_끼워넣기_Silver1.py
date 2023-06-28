# 14888_연산자_끼워넣기_Silver1
# https://www.acmicpc.net/problem/14888
import sys


def solution1():
    def operator_insert(num, idx, add, sub, mul, div):
        global max_result, min_result
        if idx == N:
            max_result = max(num, max_result)
            min_result = min(num, min_result)
        else:
            if add:
                operator_insert(num + num_list[idx], idx + 1, add - 1, sub, mul, div)
            if sub:
                operator_insert(num - num_list[idx], idx + 1, add, sub - 1, mul, div)
            if mul:
                operator_insert(num * num_list[idx], idx + 1, add, sub, mul - 1, div)
            if div:
                operator_insert(int(num / num_list[idx]), idx + 1, add, sub, mul, div - 1)

    N = int(input())
    num_list = list(map(int, sys.stdin.readline().split()))
    add, sub, mul, div = map(int, sys.stdin.readline().split())
    max_result = -(10 ** 9)
    min_result = 10 ** 9
    operator_insert(num_list[0], 1, add, sub, mul, div)
    print(max_result)
    print(min_result)


"""
무엇을 BT 할 것인가?? num_list를
언제 promising 한가?? 연산자 갯수가 0이 아닐때
언제까지? 계산 끝날때 까지 (idx 1부터 N까지)
"""


def solution2():
    N = int(input())
    nums = list(map(int, input().split()))
    opt = list(map(int, input().split()))
    result = []

    def solution(idx, operations, prior):
        if idx == N:
            result.append(prior)
        if operations[0] > 0:
            operations[0] -= 1
            solution(idx + 1, operations, prior + nums[idx])
            operations[0] += 1

        if operations[1] > 0:
            operations[1] -= 1
            solution(idx + 1, operations, prior - nums[idx])
            operations[1] += 1

        if operations[2] > 0:
            operations[2] -= 1
            solution(idx + 1, operations, prior * nums[idx])
            operations[2] += 1

        if operations[3] > 0:
            operations[3] -= 1
            if prior > 0:
                temp = prior // nums[idx]
            else:
                temp = (abs(prior) // nums[idx]) * -1
            solution(idx + 1, operations, temp)
            operations[3] += 1

    solution(1, opt, nums[0])
    print(max(result))
    print(min(result))


"""
만들 수 있는 식의 최댓값, 최솟값을 출력해야함 => 가능한 모든 값들 구해야 함
현재 가능한 모든 경우들을 재귀로 넘겨줌
이때 공유하는 operations 가 영향을 받으면 안되므로 계산마다 백트래킹 해줌
"""
