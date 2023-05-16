# 1_immigration
# https://school.programmers.co.kr/learn/courses/30/lessons/43238?language=python3
import heapq


def solution1(n, times):
    answer = 0
    times.sort()
    left, right = times[0], times[-1] * n
    while left <= right:
        mid = (left + right) // 2
        # 임의의 시간동안 몇 명의 사람을 검사 하는지 확인
        people = 0
        for time in times:
            people += mid // time
            if people >= n:  # 모든 심사관을 안 거치고 n 명 이상 심사 -> 더 짧은 시간 동안 n 명 검사 가능하므로 이후 계산 불필요
                break

        if people >= n:  # n 보다 많은 사람을 검사 -> 더 짧은 시간 동안 n 명 검사 가능 -> right 를 mid - 1 로 옮기고 answer = mid 로 설정
            answer = mid
            right = mid - 1
        else:  # n 보다 적은 사람들 검사 -> 더 많은 시간이 필요 -> left 를 mid + 1 로 옮김
            left = mid + 1

    return answer


"""
queue 를 사용하나? -> 입력 값들이 너무 큼 & 구현 실패 -> 구현 방법 못찾아서 찾아봄
이분탐색을 사용한 풀이
left, right 모두 시간을 나타냄. left 는 1, right 는 가장 길게 걸리는 시간
mid 는 임의의 시간
people += mid // term ? 예를 들어 mid = 30 이고 times 가 7, 10 이라면 총 (30//7) + (30//10) 명의 사람을 검사할 수 있다.
"""


def solution2(n, times):
    velocity = sum([1 / t for t in times])  # 1분에 처리할 수 있는 사람 수
    near = int(n / velocity)  # velocity 를 사용해 추정한 예상 소요 시간

    prior = []
    for t in times:
        cnt = near // t  # 심사관이 심사하는 사람 수
        heapq.heappush(prior, [t + cnt * t, t, cnt * t])  # 우선순위큐에는 한명 심사 시간과 누적 시간을 넣는다. 정렬 기준은 한명 추가 처리시 걸리는 시간
        n -= cnt  # 예상 시간 내에 처리된 사람 제거

    answer = near
    for i in range(n):  # 남은 사람 처리
        front = heapq.heappop(prior)
        front[0] += front[1]  # 정렬 기준 갱신
        front[2] += front[1]  # 누적시간 갱신
        heapq.heappush(prior, front)
        answer = front[2]

    return answer


"""
우선순위 큐를 사용한 풀이
정답은 항상 심사 시간의 배수
"""

n = 6
times = [7, 10]

print(solution1(n, times))
