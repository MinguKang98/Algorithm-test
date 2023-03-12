# 1_hotter
# https://school.programmers.co.kr/learn/courses/30/lessons/42626
import heapq


def solution0(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    min_scovile = scoville[0]
    while min_scovile < K:
        if len(scoville) < 2:
            return -1
        min_scovile = heapq.heappop(scoville)
        min2_scovile = heapq.heappop(scoville)
        heapq.heappush(scoville, min_scovile + min2_scovile * 2)
        min_scovile = scoville[0]
        answer += 1

    return answer


"""
음식을 섞으며 min_scovile 이 K 미만일 경우 수행을 계속한다. 이때 scovile 의 길이가 2 미만이라면, 더이상 음식을 섞을 수 없으므로,
-1 을 return 한다.
"""

scoville = [1, 2, 3, 9, 10, 12]
K = 7

# scoville = [0, 1]
# K = 7

print(solution0(scoville, K))
