# 6236_용돈_관리_Silver2
# https://www.acmicpc.net/problem/6236

N, M = map(int, input().split())
costs = [int(input()) for _ in range(N)]


def solution0():
    left = 0
    right = N - 1
    while True:
        tmep_k = sum(costs[left:right + 1])
        cnt = 0
        cur = 0
        for cost in costs:
            if cur < cost:
                cnt += 1
                cur = tmep_k
            cur -= cost
        if cnt > M:
            right += 1
        elif cnt < M:
            right -= 1
        else:
            return tmep_k


"""
K 원은 costs 의 최대보단 커야함
K 의 값은 처음부터 어느 시점까지의 합이 됨
M 에 따라서 그 시점을 정하면 됨
=> 시간 초과
"""


def solution1():
    left = min(costs)
    right = sum(costs)
    min_k = 0
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        cur = 0
        for cost in costs:
            if cur < cost:
                cnt += 1
                cur = mid
            cur -= cost

        if cnt > M or mid < max(costs):
            left = mid + 1
        else:
            right = mid - 1
            min_k = mid

    return min_k


"""
이분 탐색을 사용
내가 생각한 것은 인덱스 0 부터 인덱스 N-1 사이에 투포인터로 계싼하여 일정 부분의 합이 K 의 최소라고 생각
정답은 예산의 최소값과 예싼의 모든 합 사이의 이분탐색

이분탐색 중 계산한 cnt 가 M 보다 크면, cnt 값이 작은 것이므로 left 를 mid+1 로
cnt 가 M 보다 작으면, cnt 값이 큰 것이므로 right 를 mid-1 로
또한, K의 최소는 항상 예산의 최대보다 크므로, mid 가 max(costs) 보다 작을 때도 left 를 mid+1 로
"""

print(solution1())
