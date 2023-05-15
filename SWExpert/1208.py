#
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&contestProbId=AV139KOaABgCFAYh&categoryId=AV139KOaABgCFAYh&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=PYTHON&select-1=4&pageSize=10&pageIndex=1

def solution0(dump, heights):
    for i in range(dump):
        min_idx, min_height = 0, 100
        max_idx, max_height = 0, 1
        for idx, h in enumerate(heights):
            if h < min_height:
                min_idx = idx
                min_height = h
            if h > max_height:
                max_idx = idx
                max_height = h

        heights[min_idx] += 1
        heights[max_idx] -= 1

    print(f'#{test_case} {max(heights) - min(heights)}')


"""
bruteforce 를 통해 계산
"""


def solution1(dump, heights):
    for i in range(dump):
        heights.sort()
        heights[0] += 1
        heights[-1] -= 1
    print(f'#{test_case} {max(heights) - min(heights)}')


"""
정렬을 통해 계산
"""

T = 10
for test_case in range(1, T + 1):
    dump = int(input())
    heights = list(map(int, input().split()))
    solution0(dump, heights)
