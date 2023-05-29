# 1655_가운데를_말해요
# https://www.acmicpc.net/problem/1655
import sys
import heapq
input = sys.stdin.readline

n = int(input())
left = []
right = []
for i in range(n):
    num = int(input())
    if len(left) == len(right):
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)

    if len(left) > 0 and len(right) > 0 and left[0] * -1 > right[0]:
        left_top = heapq.heappop(left) * -1
        right_top = heapq.heappop(right)

        heapq.heappush(left, right_top * -1)
        heapq.heappush(right, left_top)

    print(left[0] * -1)

"""
말한 수들 중 중간값. 짝수라면 중간값 두개중 작은수
입력 받은 수 정렬해가며 print -> n * nlogN 이라 시간초과 예상 -> 시간 초과
그럼 어떻게 정렬 없이 중간값?
진행하며 최적해 -> greedy 나 dp 같은
우선순위 큐도 고려 => 시간 초과

하나의 힙이 아닌 최대 힙과 최소 힙을 사용해 가운데 값이 나오도록 정렬
left : top 이 최댓값인 최대 힙, right : top 이 최솟값인 최소힙
중앙값을 확인하려면 left 와 right 에 값을 번갈아 가면서 줘야함. left 의 top 이 중앙값이 됨
만약 left 의 top 이 right 의 top 보다 크다면, 두 수를 교체
"""
