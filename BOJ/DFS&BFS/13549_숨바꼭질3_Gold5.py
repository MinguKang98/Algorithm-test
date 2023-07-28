# 13549_숨바꼭질3_Gold5
# https://www.acmicpc.net/problem/13549
from collections import deque
import heapq

N, K = map(int, input().split())


def solution0():
    visited = [0 for _ in range(100001)]
    queue = [(0, N)]
    visited[N] = 1

    result = 100000
    while queue:
        cost, node = heapq.heappop(queue)
        if node == K:
            result = cost
            break

        for dx in (node * 2, node + 1, node - 1):
            if 0 <= dx <= 100000 and not visited[dx]:
                if dx == node * 2:
                    heapq.heappush(queue, (cost, dx))
                else:
                    heapq.heappush(queue, (cost + 1, dx))
                visited[dx] = 1

    return result


"""
최단거리 -> bfs
먼저 도착한 곳에 다시 가면 최소값이 아니므로 다시 갈 필요 없음
오답이라 반례에 대해 다른 문제들 참고

반례) *2 로 갈때는 cost 의 변화가 없어서 큐의 뒤로 보내면 계산이 이상해짐
 -> 우선순위 큐로 cost 조정? 시간을 우선순위 기준으로 해서 deque 같은 작동 할 거 같음
정답
"""


def solution1():
    visited = [0 for _ in range(100001)]
    queue = deque()
    queue.appendleft((N, 0))
    visited[N] = 1

    result = 100000
    while queue:
        node, cost = queue.pop()
        if node == K:
            result = cost
            break

        if 0 <= node * 2 <= 100000 and not visited[node * 2]:
            queue.append((node * 2, cost))
            visited[node * 2] = 1
        if 0 <= node - 1 <= 100000 and not visited[node - 1]:
            queue.appendleft((node - 1, cost + 1))
            visited[node - 1] = 1
        if 0 <= node + 1 <= 100000 and not visited[node + 1]:
            queue.appendleft((node + 1, cost + 1))
            visited[node + 1] = 1

        # for dx in (node * 2, node - 1, node + 1):
        #     if 0 <= dx <= 100000 and not visited[dx]:
        #         if dx == node * 2:
        #             queue.append((dx, cost))
        #         else:
        #             queue.appendleft((dx, cost + 1))
        #         visited[dx] = 1
        # 이거도 정답

    return result


"""
deque 로 푸는 방법. *2 의 우선순위를 위해 큐의 맨 뒤가 아닌 앞으로 가도록
append 를 해줌
또한 deque 를 사용할 때 node * 2, node - 1, node + 1 의 순서로 if 문 작성해야
더 빠른 방법으로 도착 ex) 4 6 (4->3->6)
"""

print(solution0())
