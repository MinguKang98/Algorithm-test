# 2580_스도쿠

import sys

# 더 빠름
def promising(num, i, j):
    # 가로줄 세로줄 중복 ㄴㄴ 3X3 안에 중복 ㄴㄴ

    if num in arr[i]:
        return False
    for k in range(9):
        if num == arr[k][j]:
            return False
    a = i // 3
    b = j // 3
    for c in range(3 * a, 3 * a + 3):
        if num in arr[c][3 * b : 3 * b + 3]:
            return False

    return True


def sudoku(x):
    if x == N:
        print("\n".join(" ".join(map(str, arr[i])) for i in range(9)))
        sys.exit()
    else:
        [i, j] = zeros[x]
        for num in range(1, 10):
            if promising(num, i, j):
                arr[i][j] = num
                sudoku(x + 1)
                arr[i][j] = 0


# google 참고. 더 느림
def is_promising_num(i, j):
    # 가로줄 세로줄 중복 ㄴㄴ 3X3 안에 중복 ㄴㄴ
    global arr
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for k in range(9):
        if arr[i][k] in num_list:
            num_list.remove(arr[i][k])
        if arr[k][j] in num_list:
            num_list.remove(arr[k][j])

    a = i // 3
    b = j // 3
    for p in range(3 * a, 3 * a + 3):
        for q in range(3 * b, 3 * b + 3):
            if arr[p][q] in num_list:
                num_list.remove(arr[p][q])

    return num_list


def sudoku2(x):
    if x == N:
        print("\n".join(" ".join(map(str, arr[i])) for i in range(9)))
        sys.exit()
    else:
        [i, j] = zeros[x]
        promising_num = is_promising_num(i, j)
        for num in promising_num:
            arr[i][j] = num
            sudoku(x + 1)
            arr[i][j] = 0


if __name__ == "__main__":
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
    zeros = [[i, j] for i in range(9) for j in range(9) if arr[i][j] == 0]
    N = len(zeros)
    sudoku(0)

"""
무엇을 BackTracking 할것인가?? -> 빈칸(0)
언제 promising 한가?? -> 행 중복 ㄴ 열 중복 ㄴ 3X3 중복 ㄴ
언제 끝나는가?? -> 빈칸이 다 채워지면
"""

"""
0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0
"""
