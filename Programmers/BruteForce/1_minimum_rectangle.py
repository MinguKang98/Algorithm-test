# 1_minimum_rectangle
# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution0(sizes):
    max_width, max_height = 0, 0
    for width, height in sizes:
        if height > width:
            width, height = height, width
        max_width = max(max_width, width)
        max_height = max(max_height, height)
    return max_width * max_height


"""
명함은 뒤집어서 넣을 수 있으므로 항상 긴 쪽을 가로, 더 짧은 쪽을 세로로 설정
다음 가로의 max 와 세로의 max 계산
"""


def solution1(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)


"""
같은 논리로 for x in sizes 에 대해 가로는 max(x), 세로는 min(x) 이므로 위와 같이 구할 수 있음
"""

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
# sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
# sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

print(solution1(sizes))
