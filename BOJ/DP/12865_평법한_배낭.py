# 12865_평법한_배낭
# https://www.acmicpc.net/problem/12865

n, k = map(int, input().split())
# items = []
# for _ in range(n):
#     w, v = map(int, input().split())
#     items.append([w, v])
items = [list(map(int, input().split())) for _ in range(n)]


def solution1():
    dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    for idx in range(1, n + 1):
        for weight in range(1, k + 1):
            item_weight, item_value = items[idx - 1]
            if item_weight <= weight:
                dp[idx][weight] = max(item_value + dp[idx - 1][weight - item_weight], dp[idx - 1][weight])
            else:
                dp[idx][weight] = dp[idx - 1][weight]

    return dp[-1][-1]


"""
인덱스의 값을 행으로, 현재 무게를 열로 정한 2차원 배열로 DP 를 수행
2차원 배열의 값인 dp[현재 인덱스][현재 무게] 는 현재 무게에서 (인덱스 - 1) 의 물건까지 사용했을 때 가지는 최대 가치를 뜻 함

인덱스 값은 (인덱스 - 1) 의 물건까지 사용한 것을 의미(1 -> 0번째만 사용, 4 -> 3번째까지 사용)
무게를 1부터 최대무게 k 까지 순회하며 (현재 인덱스 - 1) 의 물건이 들어가는 지 파악
(1) 들어간다면 -> dp[현재 인덱스][현재 무게] 는
(현재 인덱스 - 1) 의 물건의 가치 + dp[현재 인덱스 - 1][현재 무게 - (현재 인덱스 - 1) 의 물건의 무게] 와
dp[현재 인덱스 - 1][현재 무게] 중 최댓값이 됨
(2) 안들어간다면 -> dp[현재 인덱스][현재 무게] 는  dp[현재 인덱스 - 1][현재 무게] 와 동일
이를 반복 수행하여 최종 dp[-1][-1], 즉 dp[n][k] 가 문제의 답이 된다.
"""


def solution2():
    dp = [0 for _ in range(k + 1)]
    items.sort()
    for weight, value in items:
        for cur_weight in range(k, -1, -1):
            if weight <= cur_weight:
                dp[cur_weight] = max(value + dp[cur_weight - weight], dp[cur_weight])

    return dp[-1]


"""
DP 를 2차원 배열이 아닌 1차원 배열로 수행 가능
이전 행을 사용하는 것이 아닌, 현재 행을 덮어 씌우는 방식

행이 하나이므로 정렬이 되어있어야 올바른 누적해를 구할 수 있음
거꾸로 해야하는 이유 => 수정된 이전 값을 사용할 수 있음. 수정되지 않은 값을 사용하기 위해 거꾸로
"""

print(solution2())
