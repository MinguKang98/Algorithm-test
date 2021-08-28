# 14888_연산자 끼워넣기
import sys


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


if __name__ == "__main__":
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
