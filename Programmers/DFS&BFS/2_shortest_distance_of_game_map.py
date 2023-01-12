# 2_shortest_distance_of_game_map
# https://school.programmers.co.kr/learn/courses/30/lessons/1844
import sys
from collections import deque


def solution0(maps):
    n, m = len(maps), len(maps[0])

    def dfs(cur_x, cur_y, count, visited):
        if cur_x == n - 1 and cur_y == m - 1:  # 도착 하면
            return count
        else:
            # 진행할 수 없으면
            result = sys.maxsize

            # 진행할 수 있으면
            # 하
            if 0 <= cur_x + 1 <= n - 1 and 0 <= cur_y <= m - 1 and maps[cur_x + 1][cur_y] and not visited[cur_x + 1][
                cur_y]:
                visited[cur_x][cur_y] = True
                result = min(result, dfs(cur_x + 1, cur_y, count + 1, visited))
                visited[cur_x][cur_y] = False

            # 상
            if 0 <= cur_x - 1 <= n - 1 and 0 <= cur_y <= m - 1 and maps[cur_x - 1][cur_y] and not visited[cur_x - 1][
                cur_y]:
                visited[cur_x][cur_y] = True
                result = min(result, dfs(cur_x - 1, cur_y, count + 1, visited))
                visited[cur_x][cur_y] = False

            # 우
            if 0 <= cur_x <= n - 1 and 0 <= cur_y + 1 <= m - 1 and maps[cur_x][cur_y + 1] and not visited[cur_x][
                cur_y + 1]:
                visited[cur_x][cur_y] = True
                result = min(result, dfs(cur_x, cur_y + 1, count + 1, visited))
                visited[cur_x][cur_y] = False

            # 좌
            if 0 <= cur_x <= n - 1 and 0 <= cur_y - 1 <= m - 1 and maps[cur_x][cur_y - 1] and not visited[cur_x][
                cur_y - 1]:
                visited[cur_x][cur_y] = True
                result = min(result, dfs(cur_x, cur_y - 1, count + 1, visited))
                visited[cur_x][cur_y] = False

            return result

    visited = [[False for _ in range(m)] for _ in range(n)]
    answer = dfs(0, 0, 1, visited)
    if answer == sys.maxsize:
        return -1
    else:
        return answer


"""
dfs 같다. 경로 선택하며 재귀
=> RecursionError: maximum recursion depth exceeded in comparison

이전에 간 곳 가면 안됨 visited 추가하여 backtracking
=> 테스트케이스는 통과 but 오답

문제를 제대로 읽지 않아 n x m 이 아닌 4 x 4 로 구현했음. n x m 으로 수정 
=> 정답은 맞으나 효율성 테스트 timeoout
"""


def solution1(maps):
    n, m = len(maps), len(maps[0])
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.appendleft((0, 0))
    visited[0][0] = 1

    while queue:
        x, y = queue.pop()
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if 0 <= next_x < n and 0 <= next_y < m \
                    and maps[next_x][next_y] == 1 and visited[next_x][next_y] == -1:
                visited[next_x][next_y] = visited[x][y] + 1
                queue.appendleft((next_x, next_y))

    return visited[-1][-1]

"""
접근 자체가 틀렸다. 모든 경로를 탐색하는 dfs 가 아닌 bfs 에 적합
최단거리 구하는 문제는 bfs 를 사용하면 처음 끝에 도달하는 값이 정답. 반면 dfs 는 처음 끝에 도달하는 값이 답이 아닐 수 있다.

solution0 처럼 bool matrix 인 visited 를 사용했는데, visited 를 숫자로 설정하면 추가적인 코드 없이 visitied 에서
경로 거리 저장 가능
만약 도달을 했다면 visited[-1][-1] 의 값이 경로의 최단 거리일 것이고, 도달하지 못한다면 -1 일 것이다.
"""

maps = [[1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 0, 1]]

# maps = [[1, 0, 1, 1, 1],
#         [1, 0, 1, 0, 1],
#         [1, 0, 1, 1, 1],
#         [1, 1, 1, 0, 0],
#         [0, 0, 0, 0, 1]]

print(solution1(maps))
