# 4_lifeboat
# https://school.programmers.co.kr/learn/courses/30/lessons/42885
from collections import deque


def solution0_1(people, limit):
    people.sort()
    answer = 1
    temp_weight = limit - people[0]
    for i in range(1, len(people)):
        if temp_weight - people[i] >= 0:
            temp_weight -= people[i]
        else:
            answer += 1
            temp_weight = limit - people[i]

    return answer


"""
한보트에 작은 거 부터 태우기
=> 오답 why? 문제를 잘못 읽음. 보트에 최대 두 명만 태울 수 있음
"""


def solution0_2(people, limit):
    people.sort()
    answer = 0
    left, right = 0, len(people) - 1
    while left < right:
        if people[left] + people[right] <= limit:
            answer += 1
            left += 1
            right -= 1
        else:
            right -= 1

    return len(people) - answer


"""
보트에 최대 두 명 태울 수 있으므로 작은 것과 큰 것을 최대한 같이 태우기
투포인터로 함께 탈 수 없으면 right 만 이동, 탈 수 있으면 체크 후 left, right 모두 이동하기
체크 못한 사람은 모두 혼자 타야하므로 최종 답은 len - answer
"""


def solution1(people, limit):
    answer = 0
    deque_people = deque(sorted(people))

    while deque_people:
        left = deque_people.popleft()
        if not deque_people:
            return answer + 1
        right = deque_people.pop()
        if left + right > limit:
            deque_people.appendleft(left)
        answer += 1

    return answer

"""
queue 를 사용한 풀이이다. queue 의 left 와 right 를 사용해 합이 limit 보다 크다면 보트에는 right 만 탈 수 있으므로
left 는 다시 appendleft 를 통해 queue 에 넣는다.
"""


# people = [70, 50, 80, 50]
# limit = 100

people = [70, 80, 50]
limit = 100

print(solution0_2(people, limit))
