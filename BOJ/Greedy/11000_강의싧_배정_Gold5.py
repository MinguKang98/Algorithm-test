# 11000_강의싧_배정_Gold5
# https://www.acmicpc.net/problem/11000
import heapq

N = int(input())
courses = [list(map(int, input().split())) for _ in range(N)]


def solution0():
    answer = 1
    courses.sort(key=lambda x: (x[1], x[0]))
    queue = []
    heapq.heappush(queue, (courses[0][1], courses[0][0]))
    courses.sort(key=lambda x: (x[0], x[1]))

    for start, end in courses[1:]:
        if queue[0][0] <= start:
            heapq.heappop(queue)
            heapq.heappush(queue, (end, start))
        else:
            answer += 1
            heapq.heappush(queue, (end, start))

    return answer


"""
최소 강의실
끝나는 시간으로 정렬 후, 끝나는 시간 기준인 priority queue 사용해서 강의실 세기?
탐색 강의의 시작시간과 priority queue 의 front 의 종료 시간 비교
1. 종료시간 <= 시작시간 : queue 의 front 제거 후 탐색 강의 삽입
2. 종료시간 > 시작시간 : 강의실 추가 + queue 에 삽입

오답 => 예외있나?
4
1 3
2 8
8 9
3 10
에 대해서 2 가 아닌 3이 나옴

queue 는 끝나는 순, 탐색하는 강의는 시작순으로 정렬
=> 오답
"""


def solution1():
    answer = 1
    courses.sort()
    queue = []
    heapq.heappush(queue, (courses[0][1], courses[0][0]))

    for start, end in courses[1:]:
        if queue[0][0] <= start:
            heapq.heappop(queue)
            heapq.heappush(queue, (end, start))
        else:
            answer += 1
            heapq.heappush(queue, (end, start))

    return answer


"""
풀이방법 맞았는데 정렬때문에 틀린듯
=> 시간초과 => pypy3 로 변경 => 정답
"""


def solution2():
    # answer = 1
    courses.sort()
    queue = []
    heapq.heappush(queue, courses[0][1])

    for start, end in courses[1:]:
        if queue[0] <= start:
            heapq.heappop(queue)
            heapq.heappush(queue, end)
        else:
            # answer += 1
            heapq.heappush(queue, end)

    # return answer
    return len(queue)


"""
queue 에서 시작 시간은 필요 없으므로 간략화
answer 안쓰고 len(queue) 도 가능
"""

print(solution0())
