# 19598_최소_회의실_개수_Gold5
# https://www.acmicpc.net/problem/19598
import heapq

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]


def solution0():
    meetings.sort()
    queue = []
    heapq.heappush(queue, meetings[0][1])
    cnt = 1

    for start, end in meetings[1:]:
        top = queue[0]
        if start >= top:
            heapq.heappop(queue)
            heapq.heappush(queue, end)
        else:
            heapq.heappush(queue, end)
            cnt += 1

    return cnt


"""
최소 회의실 개수
탐색할 회의들은 시작순으로, 우선순위 큐는 종료순으로 
제일 빨리 종료되는 회의와 탐색한 회의의 시작 시간을 비교
시작 시간이 종료 시간 이후라면, 같은 강의실 사용이 가능하므로 heappop 후 heappush 
이전이라면, 다른 강의실 사용해야 하므로 heappush 후 강의실 수 증가시킴
"""


def solution1():
    meetings.sort()
    queue = []

    for start, end in meetings:
        if queue and start >= queue[0]:
            heapq.heappop(queue)
        heapq.heappush(queue, end)

    return len(queue)


"""
solution0 과 같은 풀이지만 다른 구현. 
heap 의 크기가 결국 강의실 개수
"""

print(solution0())
