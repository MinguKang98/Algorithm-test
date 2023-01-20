# 1_undone_player
# https://school.programmers.co.kr/learn/courses/30/lessons/42576
from collections import Counter, defaultdict


def solution0(participant, completion):
    a = Counter(participant)
    b = Counter(completion)
    c = a - b
    return list(c.keys())[0]


"""
Counter 가 연산이 가능하다는 것을 사용한 풀이
"""


def solution1(participant, completion):
    dict = defaultdict(int)
    for p in participant:
        dict[p] += 1

    for c in completion:
        dict[c] -= 1

    result = [k for k, v in dict.items() if v == 1]
    return result[0]


participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

print(solution1(participant, completion))
