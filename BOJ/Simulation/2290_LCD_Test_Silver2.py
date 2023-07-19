# 2290_LCD_Test_Silver2
# https://www.acmicpc.net/problem/2290

s, n = input().split()
s = int(s)


def solution0():
    def horizontal(start, row, _list):
        for j in range(1, s + 1):
            _list[row][start + j] = '-'

    def vertical1(start, _list):
        for j in range(1, s + 1):
            _list[j][start] = '|'

    def vertical2(start, _list):
        for j in range(s + 2, 2 * s + 2):
            _list[j][start] = '|'

    def save(start, num, _list):
        if num in '23567890':
            horizontal(start, 0, _list)
        if num in '2345689':
            horizontal(start, s + 1, _list)
        if num in '2356890':
            horizontal(start, 2 * s + 2, _list)
        if num in '456890':
            vertical1(start, _list)
        if num in '12347890':
            vertical1(start + s + 1, _list)
        if num in '2680':
            vertical2(start, _list)
        if num in '134567890':
            vertical2(start + s + 1, _list)

    save_list = [[' ' for _ in range((s + 3) * len(n))] for _ in range(2 * s + 3)]

    for idx, num in enumerate(n):
        save(idx * (s + 3), num, save_list)

    for i in range(len(save_list)):
        print(''.join(save_list[i]))


"""
세로 하나 s개, 가로 하나 s개
전부 구현해도 되지만, in 을 사용해서 구현 코드 줄일 수 있음
"""

solution0()
