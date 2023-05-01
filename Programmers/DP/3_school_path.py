# 3_school_path
# https://school.programmers.co.kr/learn/courses/30/lessons/42898

def solution0(m, n, puddles):
    grid = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    grid[1][1] = 1
    for i, j in puddles:
        grid[j][i] = -1

    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if i == 1 and j == 1:  # 집이면 통과
                continue
            if grid[j][i] == -1:  # 웅덩이면 통과
                continue

            left = grid[j][i - 1]
            if left == -1:
                left = 0
            up = grid[j - 1][i]
            if up == -1:
                up = 0
            grid[j][i] = left + up

    return grid[n][m] % 1000000007


"""
현재 위치는 왼쪽과 위쪽의 값의 합
초기값 = 0, 웅덩이 = -1, 나머지는 현재 위치에 지나가는 경로 수
합을 쌓아가는 타뷸레이션 방식
"""


def solution1(m, n, puddles):
    memo = {}
    for puddle in puddles:
        memo[tuple(puddle)] = -1
    memo[(1, 1)] = 1

    def func(m, n):
        if m < 1 or n < 1:
            return 0
        if (m, n) in memo:
            return memo[(m, n)]

        left = func(m - 1, n)
        up = func(m, n - 1)
        if left == -1:
            left = 0
        if up == -1:
            up = 0

        x = left + up
        memo[(m, n)] = x
        return x

    return func(m, n) % 1000000007


"""
재귀를 사용한 메모이제이션 방식
"""

m = 4
n = 3
puddles = [[2, 2]]

print(solution1(m, n, puddles))
