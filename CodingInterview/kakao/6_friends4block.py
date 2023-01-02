# 6_friends4block
# https://school.programmers.co.kr/learn/courses/30/lessons/17679
from typing import List


class Solution:
    # Solution0 - fail
    def friends4block0(self, m: int, n: int, board: List[str]) -> int:
        def is2x2(row: int, column: int) -> bool:
            return board_list[row][column] == board_list[row][column + 1] \
                   and board_list[row + 1][column] == board_list[row + 1][column + 1] \
                   and board_list[row][column] == board_list[row + 1][column + 1]

        def is2x2Exist(m: int, n: int) -> bool:
            for row in range(m - 1):
                for column in range(n - 1):
                    if is2x2(row, column):
                        return True
            return False

        board_list = []
        for b in board:
            board_list.append(list(b))
        count = 0
        while is2x2Exist(m, n):  # board 에 square 없을 때 까지

            delete_set = set()
            # 2x2 탐색
            for i in range(m - 1):
                for j in range(n - 1):
                    if is2x2(i, j):
                        delete_set.add((i, j))

            # 2x2 모두 삭제 & 삭제 count
            for row, column in delete_set:
                for i in range(2):
                    for j in range(2):
                        board_list[row + i][column + j] = '#'
                        count += 1

            # 블럭 밀기

            for _ in range(m):
                for i in range(m - 1):
                    for j in range(n):
                        if board_list[i + 1][j] == '#':
                            board_list[i + 1][j], board_list[i][j] = board_list[i][j], board_list[i + 1][j]

        return count

    """
    로직은 유사하지만 구현 방법이 틀린 것 같다.
    """

    def friends4block1(self, m: int, n: int, board: List[str]) -> int:
        board = [list(x) for x in board]

        matched = True
        while matched:
            # 일치 여부 탐색
            matched = []
            for i in range(m - 1):
                for j in range(n - 1):
                    if board[i][j] == \
                            board[i][j + 1] == \
                            board[i + 1][j + 1] == \
                            board[i + 1][j] != '#':
                        matched.append([i, j])

            # 일치한 위치 삭제
            for i, j in matched:
                board[i][j] = board[i + 1][j] = board[i][j + 1] = board[i + 1][j + 1] = '#'

            # 빈 공간 블럭 처리
            for _ in range(m):
                for i in range(m - 1):
                    for j in range(n):
                        if board[i + 1][j] == '#':
                            board[i + 1][j], board[i][j] = board[i][j], '#'

        return sum(x.count('#') for x in board)


m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]

# m = 6
# n = 6
# board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

print(Solution().friends4block1(m, n, board))
