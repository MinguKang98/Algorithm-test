# 1_target_number
# https://school.programmers.co.kr/learn/courses/30/lessons/43165?language=python3
from itertools import product


def dfs(current, target, depth):
    if depth == len(numbers):
        return current == target
    else:
        return dfs(current + numbers[depth], target, depth + 1) + \
               dfs(current - numbers[depth], target, depth + 1)


def solution1(numbers, target):
    answer = dfs(0, target, 0)
    return answer


"""
타겟 넘버를 만드는 경우를 구하기 위해 dfs 를 사용했다.
dfs 가 끝에 도달했을 때, 계산한 값이 target 과 같다면 1, 같지 않다면 0 을 리턴한다.
나머지 경우는 다음 값을 더했을 때와 뺏을 때 dfs 의 합을 리턴하는데, 이 값은 재귀로 인해 타겟 넘버를 만드는 경우의 수와 같게 된다.
"""


def solution2(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)


"""
itertools 의 product 를 사용해 모든 계산의 경우의 수를 가지는 리스트인 s 를 생성하고, s 에서 target 의 갯수를 센다.
"""

# numbers = [1, 1, 1, 1, 1]
# target = 3

numbers = [4, 1, 2, 1]
target = 4

print(solution2(numbers, target))
