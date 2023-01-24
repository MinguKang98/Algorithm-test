# 4_camouflage
# https://school.programmers.co.kr/learn/courses/30/lessons/42578
from collections import defaultdict
from itertools import combinations


def solution0(clothes):
    clothes_dict = defaultdict(list)
    for name, kind in clothes:
        clothes_dict[kind].append(name)

    count_list = [len(c) for c in clothes_dict.values()]

    if len(count_list) == 1:
        return count_list[0]
    else:
        result = sum(count_list)
        for i in range(2, len(count_list) + 1):  # 종류의 갯수
            comb = list(combinations(count_list, i))  # 가능한 조합
            for c in comb:
                temp = 1
                for num in c:
                    temp *= num
                result += temp
    return result


"""
count_list 의 가능한 combination 을 모두 구한 후 그들의 곱을 모두 더함

testcase 1 시간초과 ??? => n^3 의 복잡도를 가져 위험함
"""


def solution1(clothes):
    clothes_dict = defaultdict(list)
    for name, kind in clothes:
        clothes_dict[kind].append(name)

    count_list = [len(c) for c in clothes_dict.values()]

    temp = 1
    for num in count_list:
        temp *= num + 1

    return temp - 1


"""
가능한 combination 을 모두 구한 후 그들의 곱을 더한 값과 count_list 의 element 에 1을 더한 값들을
모두 곱한 후 1을 뺀 값은 같다.
why?? 해당 종류의 옷을 입지 않는 경우를 생각하기 위해 1 을 더하고, 아무 것도 입지 않는 경우를 제외하기 위해 모두 곱한 
값에서 1을 뺀다.
"""

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
# clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]

print(solution0(clothes))
