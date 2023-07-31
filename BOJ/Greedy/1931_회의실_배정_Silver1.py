# 1931_회의실_배정_Silver1
# https://www.acmicpc.net/problem/1931
from collections import deque

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]


def solution0_1():
    result = 0
    meetings.sort()
    for idx, meeting in enumerate(meetings):
        temp = 1
        queue = deque()
        queue.appendleft(meeting[1])
        while queue:
            pre_end = queue.pop()
            for s, e in meetings:
                if s >= pre_end:
                    temp += 1
                    queue.appendleft(e)
                    break
        result = max(result, temp)

    return result


"""
시작시간을 정렬 후 큐로 풀이
시간초과
"""


def solution0_2():
    meetings.sort(key=lambda x: x[1])

    result = 1
    queue = deque()
    queue.appendleft(meetings[0][1])
    temp_meetings = meetings
    while queue:
        pre_end = queue.pop()
        for idx, meeting in enumerate(temp_meetings):
            s, e = meeting
            if s >= pre_end:
                result += 1
                queue.appendleft(e)
                temp_meetings = temp_meetings[idx:]
                break

    return result


"""
종료시간을 정렬 후 큐로 풀이
시간초과
"""


def solution0_3():
    meetings.sort(key=lambda x: (x[1], x[0]))
    result = 1
    pre_end = meetings[0][1]
    for start, end in meetings[1:]:
        if start >= pre_end:
            result += 1
            pre_end = end

    return result


"""
종료시간을 정렬 후 순회하며 연결 안되는 거 안세기
처음에 정렬을 x[1] 에 대해서만 해서 99퍼 오답
x[0] 도 정렬하니 정답

그리디로 풀어야 했던 이유 : 종료시간 기준 정렬했을 때 시작 가능한 것만
고르면 최대 회의 수를 구할 수 있기 때문
"""

print(solution0_3())
