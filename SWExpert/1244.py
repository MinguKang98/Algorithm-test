# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&contestProbId=AV15Khn6AN0CFAYD&categoryId=AV15Khn6AN0CFAYD&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=PYTHON&select-1=4&pageSize=10&pageIndex=1
from collections import deque

# T = int(input())
# for test_case in range(1, T + 1):
#     num, chg = input().split()
#     chg = int(chg)
#
#     now = set([num])
#     next = set()
#
#     for _ in range(chg):
#         while now:
#             s = now.pop()
#             s = list(s)
#             for i in range(len(num) - 1):
#                 for j in range(i + 1, len(num)):
#                     s[i], s[j] = s[j], s[i]
#                     next.add(''.join(s))
#                     s[i], s[j] = s[j], s[i]
#         now, next = next, now
#
#     print(f"#{test_case} {max(map(int, now))}")

"""
bruteforce 를 통해 모든 교환값들을 구한 후, 그 중 최대값이 정답
"""


def change(numbers, cnt):
    global result

    temp = int(''.join(numbers))
    if temp in result[cnt]:
        return
    else:
        result[cnt].append(temp)

    if cnt == 0:
        return

    for i in range(n):
        for j in range(i + 1, n):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            change(numbers, cnt - 1)
            numbers[i], numbers[j] = numbers[j], numbers[i]


T = int(input())
for test_case in range(1, T + 1):
    numbers, cnt = input().split()
    numbers = list(numbers)
    n = len(numbers)
    result = [[] for _ in range(int(cnt) + 1)]

    change(numbers, int(cnt))

    print(f'#{test_case} {max(result[0])}')

"""
재귀를 사용하여 모든 교환값들을 구현. 이때 값을 기억하는 list를 사용해 한번 구한 값은 다시 계산 ㄴㄴ
"""
