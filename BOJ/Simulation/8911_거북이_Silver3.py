# 8911_거북이_Silver3
# https://www.acmicpc.net/problem/8911

T = int(input())
turtle_moves = [input() for _ in range(T)]


def solution0():
    def move(str_move):
        x_list = [0]
        y_list = [0]
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        temp = 0  # 방향 나타내는 숫자
        for m in str_move:
            if m == 'F':
                x_list.append(x_list[-1] + directions[temp][0])
                y_list.append(y_list[-1] + directions[temp][1])
            if m == 'B':
                x_list.append(x_list[-1] + directions[(temp + 2) % 4][0])
                y_list.append(y_list[-1] + directions[(temp + 2) % 4][1])
            if m == 'L':
                temp = (temp + 3) % 4
            if m == 'R':
                temp = (temp + 1) % 4

        return (max(x_list) - min(x_list)) * (max(y_list) - min(y_list))

    for turtle_move in turtle_moves:
        print(move(turtle_move))


"""
거북이 지나간 영역 포함하는 가장 작은 직사각형 넓이
이동 좌표들 x 따로 y 따로 누적
x 최대 최소의 차 와 y 최대 최소의 차 의 곲이 직사각형 최소 넓이. 넓이 0 인 경우도 커버 가능 
"""

solution0()
