# 1992_쿼드트리_Silver1
# https://www.acmicpc.net/problem/1992
import math

N = int(input())
matrix = [list(input()) for _ in range(N)]


def solution0():
    def check(i, j, dist):
        if matrix[i][j] in ('0', '1') and \
                matrix[i][j] == matrix[i][j + dist] == matrix[i + dist][j] == matrix[i + dist][j + dist]:
            return matrix[i][j]
        else:
            return f'({matrix[i][j]}{matrix[i][j + dist]}{matrix[i + dist][j]}{matrix[i + dist][j + dist]})'

    temp = 2
    num = N
    while num > 1:
        for i in range(0, N, temp):
            for j in range(0, N, temp):
                matrix[i][j] = check(i, j, temp // 2)
        temp *= 2
        num /= 2

    return matrix[0][0]


"""
재귀 사용한 완탐인거 같은데 -> bottom up 으로 하자
왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래 로 나누어 압축
=> 오답
4
0000
1111
0000
1111
의 경우 (0011) 이 네 곳에서 같은데, 이를 합쳐버리면 안되고 연결해야함
즉, 합치는 건 숫자 하나일때만! => 정답
"""


def solution1():
    def quad_tree(x, y, dist):
        check = matrix[x][y]
        for i in range(x, x + dist):
            for j in range(y, y + dist):
                if check != matrix[i][j]:
                    check = "-1"
                    break

        if check == '-1':  # 다르면 잘라서
            print("(", end='')
            dist //= 2
            quad_tree(x, y, dist)  # 왼쪽 위
            quad_tree(x, y + dist, dist)  # 오른쪽 위
            quad_tree(x + dist, y, dist)  # 왼쪽 아래
            quad_tree(x + dist, y + dist, dist)  # 오른쪽 아래
            print(")", end='')
        elif check == '1':
            print(1, end='')
        else:
            print(0, end='')

    quad_tree(0, 0, N)


"""
재귀로 풀이
"""

# print(solution0())
solution1()