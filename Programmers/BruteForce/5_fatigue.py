# 5_fatigue
# https://school.programmers.co.kr/learn/courses/30/lessons/87946
from itertools import permutations


def solution0(k, dungeons):
    result = []
    for paths in permutations(dungeons):
        temp = k
        count = 0
        for p in paths:
            if temp >= p[0]:
                temp -= p[1]
                count += 1
            else:
                break
        result.append(count)

    return max(result)


"""
permutations 를 사용해 가능한 탐사 순서를 모두 구하고, 각각의 순서에 대해 조건에 따른 count 값을 구한다.
"""

answer = 0


def solution1(k, dungeons):
    def dfs(current, cnt):
        global answer
        if cnt > answer:
            answer = cnt

        for idx, dungeon in enumerate(dungeons):
            if current >= dungeon[0] and not visited[idx]:
                visited[idx] = 1
                dfs(current - dungeon[1], cnt + 1)
                visited[idx] = 0

    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0)
    return answer


"""
backtracking 을 사용한 방법이다. dfs 를 사용한 backtracking 으로 모든 경로의 cnt 값을 구하고, global answer 보다
cnt 값이 더 크다면 answer 를 갱신시킨다.
"""

k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]

print(solution1(k, dungeons))
