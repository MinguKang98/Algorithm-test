# 2_ponketmon
# https://school.programmers.co.kr/learn/courses/30/lessons/1845
from collections import Counter


def solution0(nums):
    n = len(nums)
    count_dict = Counter(nums)
    ponketmon_cnt = len(count_dict.keys())
    return min(n // 2, ponketmon_cnt)


"""
겹치는 값들을 갯수로 표현하기 위해 counter 객체 사용
폰켓몬 종류의 갯수가 n/2 보다 많으면 n/2 가, 작으면 폰켓몬 종류의 갯수가 정답이 된다. 
=> if-else 문도 가능하지만 min 으로도 표현 가능 
"""


def solution1(nums):
    return min(len(nums) / 2, len(set(nums)))


"""
필요한 것의 counter 의 key 값들이므로 counter 를 쓸 필요 없이 set 을 써서 풀이 가능
"""

# nums = [3, 1, 2, 3]
# nums = [3, 3, 3, 2, 2, 4]
nums = [3, 3, 3, 2, 2, 2]

print(solution0(nums))
