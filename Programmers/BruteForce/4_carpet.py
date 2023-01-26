# 4_carpet
# https://school.programmers.co.kr/learn/courses/30/lessons/42842
import math


def solution0(brown, yellow):
    total = brown + yellow
    for height in range(1, int(math.sqrt(total)) + 1):
        if total % height == 0:
            width = total // height
            if (height - 2) * (width - 2) == yellow:
                return [width, height]


"""
가로와 세로가 있을 때, 가로 * 세로 = brwon + yellow 이고 yellow = (가로-2) * (세로-2) 이다.
"""

# brown = 10
# yellow = 2

# brown = 8
# yellow = 1

brown = 24
yellow = 24

print(solution0(brown, yellow))
