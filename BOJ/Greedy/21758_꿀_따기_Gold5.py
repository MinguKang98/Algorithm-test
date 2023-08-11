# 21758_꿀_따기_Gold5
# https://www.acmicpc.net/problem/21758

N = int(input())
honeys = list(map(int, input().split()))


def solution0():
    result1 = sum1 = sum(honeys[2:]) * 2
    for i in range(2, N - 1):  # 왼 -> 오
        sum1 = sum1 - honeys[i] * 2 + honeys[i - 1]
        result1 = max(result1, sum1)

    result2 = sum2 = sum(honeys[1:-1]) + honeys[1]
    for i in range(2, N - 1):  # 왼 -> 중 <- 오
        sum2 = sum2 - honeys[i - 1] + honeys[i]
        result2 = max(result2, sum2)

    honeys.reverse()
    result3 = sum3 = sum(honeys[2:]) * 2
    for i in range(2, N - 1):  # 오 -> 왼
        sum3 = sum3 - honeys[i] * 2 + honeys[i - 1]
        result3 = max(result3, sum3)

    return max(result1, result2, result3)


"""
1 10 1 5 10

15 15

세가지 경우의 수
1. 벌들 왼쪽, 벌통 오른쪽
2. 벌들 오른쪽, 벌통 왼쪽
이때 1,2 의 경우 벌들은 연속한 위치에 존재하지 않을 수 있음 ex) 1 10 1 5 10
3. 벌들 양 끝, 벌통 중간 어딘가
"""

print(solution0())
