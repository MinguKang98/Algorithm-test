# 12851_숨바꼭질2_Gold4
# https://www.acmicpc.net/problem/12851
from collections import deque

N, K = map(int, input().split())


def solution0():
    visited = [0] * 100001
    queue = deque()
    queue.appendleft((N, 0))

    time = 0
    cnt = 0
    while queue:
        cur_loc, cur_time = queue.pop()
        if cur_loc < 0 or cur_loc > 100000:
            continue

        if visited[cur_loc]:
            continue

        if cur_loc != K:
            visited[cur_loc] = 1
        else:
            if cnt == 0:
                time = cur_time
                cnt += 1
            elif time == cur_time:
                cnt += 1
            continue

        queue.appendleft((cur_loc - 1, cur_time + 1))
        if cur_loc < K:
            queue.appendleft((cur_loc + 1, cur_time + 1))
            queue.appendleft((cur_loc * 2, cur_time + 1))

    print(time)
    print(cnt)


"""`
N은 현재 위치에서 +1, -1, *2 로 이동 가능
가장 빠른 시간 + 방법 몇 개

최단거리는 bfs 로
visited 필요 -> 1. bfs 이므로, 2. 특정 위치에 처음 도착했을 때가 최소값이므로
나중에 도달한 것은 최소시간이 될 수 없음

현재가 K 보다 작으면 -1, +1, *2 
현재가 K 보다 크면 -1
50퍼 정도 정답 이후 오답
"""


def solution1():
    visited = [0] * 100001
    queue = deque()
    queue.appendleft(N)

    time = 100001
    cnt = 0
    while queue:
        cur_loc = queue.pop()
        cur_cnt = visited[cur_loc]

        if cur_cnt > time:
            continue

        if cur_loc == K:
            if time == 100001:
                time = cur_cnt

            if cur_cnt == time:
                cnt += 1

        for nx in (cur_loc - 1, cur_loc + 1, cur_loc * 2):
            if 0 <= nx < 100001 and (not visited[nx] or visited[nx] == cur_cnt + 1):
                visited[nx] = cur_cnt + 1
                queue.appendleft(nx)

    print(time)
    print(cnt)


"""
visited 에 방문 여부뿐만 아니라 방문 횟수까지 저장
visited[nx] == cur_cnt + 1 를 체크하지 않았음
=> 동일한 탐색횟수를 가진 곳을 탐색해야 이미 탐색한 곳도 탐색해서 감. 이때 
동일한 탐색횟수란 앞으로 갈 곳의 횟수가 현재 횟수보다 1 큰 것.
중복탐색의 bfs 를 다룬 문제이므로 풀이 방식 기억할 것
"""

solution0()
