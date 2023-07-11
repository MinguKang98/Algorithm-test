# 1038_감소하는_수_Gold5
# https://solved.ac/search?query=1038
from itertools import combinations

N = int(input())


def solution1():
    result = []
    for i in range(1, 11):
        for comb in combinations(range(0, 10), i):
            comb = list(comb)
            comb.sort(reverse=True)
            result.append(int("".join(map(str, comb))))
    result.sort()

    # try:
    #     return result[N]
    # except:
    #     return -1

    if N < len(result):
        return result[N]
    else:
        return -1


"""
무슨 유형인가?? => 이진탐색? 브루트포스?
브루트포스는 시간 너무 오래걸려 아닐 거 같은데

브루트포스 맞았음
안 되는 수는 어떻게 판별하는지 생각 못했는데 감소하는 수의 마지막 값은 9876543210 이었음
조합을 사용해서 모든 감소하는 수 생성하면 되는 풀이

try-except 나 if-else 취향껏 사용
"""


def solution2():
    result = []

    def make_num(num, i):  # num 까지의 숫자들 중 i 개를 사용한 감소하는 수 생성하기
        if i > 10:
            return

        result.append(num)
        for j in range(0, num % 10):  # num 의 마지막 자리수보다 작은 수가 뒤에 올 수 있으므로 합쳐줌
            make_num(10 * num + j, i + 1)

    for num in range(10):
        make_num(num, 1)
    result.sort()

    if N < len(result):
        return result[N]
    else:
        return -1


"""
itertools 없는 풀이
재귀를 사용하여 모든 감소하는 수를 생성함

"""

print(solution1())
