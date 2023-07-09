# 1789_수들의_합_Silver5
# https://www.acmicpc.net/problem/1789
import math

S = int(input())


def solution1():
    temp = int(math.sqrt(2 * S))

    while True:
        temp_sum = temp * (temp + 1) // 2
        if temp_sum <= S:
            temp += 1
        else:
            break
    return temp - 1


"""
1부터 A 까지의 합 중에서 S보다 작으며 가장 가까운 A 가 N 인거 같음
2S 의 제곱근 부터 탐색 시작
"""


def solution2():
    count = 0
    total = 0

    while True:
        count += 1
        total += count
        if total > S:
            break

    return count - 1


"""
그리디를 사용한 접근법

비슷한 방법이지만 1부터 탐색함
"""

print(solution1())
