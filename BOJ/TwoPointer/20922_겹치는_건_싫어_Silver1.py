# 20922_겹치는_건_싫어_Silver1
# https://www.acmicpc.net/problem/20922
from collections import defaultdict

N, K = map(int, input().split())
nums = list(map(int, input().split()))


def solution0():
    def check_duplicate(_dict):
        for num in _dict.keys():
            if _dict[num] > K:
                return True
        return False

    num_dict = defaultdict(int)
    num_dict[nums[0]] += 1
    result = 0
    left, right = 0, 0
    while True:
        if check_duplicate(num_dict):
            num_dict[nums[left]] -= 1
            left += 1
            continue

        result = max(result, right - left + 1)
        if right >= N - 1:
            break
        right += 1
        num_dict[nums[right]] += 1

    return result


"""
투포인터로 풀이
시간초과
"""


def solution1():
    num_dict = defaultdict(int)
    result = 0
    left, right = 0, 0
    while right < N:
        if num_dict[nums[right]] < K:
            num_dict[nums[right]] += 1
            right += 1
        else:
            num_dict[nums[left]] -= 1
            left += 1
        result = max(result, right - left)

    return result


"""
다른 풀이 보며 힌트 -> 모든 dict 를 검사할 필요없이 추가할 때만 검사
추가할 숫자의 갯수는 K 미만이어야 함
"""

print(solution0())
