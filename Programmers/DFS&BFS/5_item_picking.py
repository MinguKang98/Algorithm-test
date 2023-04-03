# 5_item_picking
# https://school.programmers.co.kr/learn/courses/30/lessons/87694
from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    area = [[0 for _ in range(102)] for _ in range(102)]
    for x1, y1, x2, y2 in rectangle:
        for i in range(2 * x1, 2 * x2 + 1):
            for j in range(2 * y1, 2 * y2 + 1):
                area[i][j] = 1

    for x1, y1, x2, y2 in rectangle:
        for i in range(2 * x1 + 1, 2 * x2):
            for j in range(2 * y1 + 1, 2 * y2):
                area[i][j] = 0

    itemX, itemY = itemX * 2, itemY * 2
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    queue = deque()
    queue.appendleft([characterX * 2, characterY * 2, 0])
    visited = [[0 for _ in range(102)] for _ in range(102)]
    while queue:
        cur_x, cur_y, cost = queue.pop()
        if cur_x == itemX and cur_y == itemY:
            answer = cost // 2
            break

        for i, j in move:
            x = cur_x + i
            y = cur_y + j
            if area[x][y] and visited[x][y] == 0:
                queue.appendleft([x, y, cost + 1])
                visited[x][y] = 1

    return answer


"""
테두리만 최단거리로 => bfs
1. 50x50 배열에서 테두리를 먼저 생성
2. 현재 점부터 갈 수 있는 부분 bfs 로 진행해서 목표지점 나올 때까지

아이디어는 맞지만 구현 ㄴㄴ

우선 모두 2배를 해서 생각 => 빈칸 만들 다 오류 생김
테두리를 만드는 법은 주어진 도형을 1로 모두 채운 후, 한칸씩 짝은 도형을 0으로 채움
목적지에 도착하면 cost 를 2로 나누어 answer 에 대입

테두리를 못 구한 것과 두배를 생각 못한 것이 아쉽다. 나머지는 맞게 생각함
"""

rectangle = [[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]]
characterX = 1
characterY = 3
itemX = 7
itemY = 8

print(solution(rectangle, characterX, characterY, itemX, itemY))
