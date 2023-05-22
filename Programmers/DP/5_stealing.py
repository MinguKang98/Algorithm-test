# 5_stealing
# https://school.programmers.co.kr/learn/courses/30/lessons/42897

def solution0(money):
    n = len(money)
    dp1 = [-1 for _ in range(n)]  # 처음 포함 dp
    dp2 = [-1 for _ in range(n)]  # 마지막 포함 dp

    # 0 ~ n-2
    for idx in range(n - 1):
        if idx == 0:
            dp1[idx] = money[0]
        elif idx == 1:
            dp1[idx] = max(money[0], money[1])
        else:
            dp1[idx] = max(dp1[idx - 2] + money[idx], dp1[idx - 1])

    # 1 ~ n-1
    for idx in range(1, n):
        if idx == 1:
            dp2[idx] = money[1]
        elif idx == 2:
            dp2[idx] = max(money[1], money[2])
        else:
            dp2[idx] = max(dp2[idx - 2] + money[idx], dp2[idx - 1])

    return max(dp1[n - 2], dp2[n - 1])


"""
최대로 털 수 있는 집의 수 n//2
집들의 이차원배열 사용 => 시간 초과 날 듯

일차원 배열 => i 번째 까지의 최대 합 
이전 함들과 현재를 여차저차 하여 현재 위치 최대 합 구함
근데 원형이라 처음과 마지막은 이웃하는 사이인 것을 고려해야함

힌트 얻어서 풀음
원형을 고려하면
(1) 처음 집을 포함하고 마지막 집을 제외할 때 값
(2) 처음 집을 제외하고 마지막 집을 포함할 때 값
(1) 과 (2) 를  
"""

money = [1, 2, 3, 1]

print(solution0(money))
