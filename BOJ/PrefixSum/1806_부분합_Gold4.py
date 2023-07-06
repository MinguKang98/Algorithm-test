# 1806_부분합_Gold4
# https://www.acmicpc.net/problem/1806

N, S = map(int, input().split())
nums = list(map(int, input().split()))


def solution1():
    answer = N
    temp = 0
    right = 0

    if sum(nums) < S:
        return 0

    for left in range(N):
        while temp < S and right < N:
            temp += nums[right]
            right += 1

        if temp >= S:
            answer = min(answer, right - left)
        temp -= nums[left]

    return answer


"""
누적합 보고 푸는 방법 생각남 => 배열에 i 까지의 합 넣은 후 i 의 값과 j 의 값을 빼면 해당 구간의 누적값
굳이 누적합 배열이 필요 없을 듯 하여 투포인터 생각 => 정확한 투포인터 사용법은 풀이를 참조

투포인터 사용법을 익혀야 할 듯
"""


def solution2():
    answer = 100000
    temp = 0
    left, right = 0, 0

    while True:
        if temp >= S:
            answer = min(answer, right - left)
            temp -= nums[left]
            left += 1
        elif right == N:
            break
        else:
            temp += nums[right]
            right += 1

    if answer == 100000:
        return 0

    return answer


"""
다른 방식의 투포인터
"""


def solution3():
    prefix = [0] * (N + 1)

    for i in range(1, N + 1):
        prefix[i] = prefix[i - 1] + nums[i - 1]

    answer = 100000
    left, right = 0, 1
    while left < N:
        if prefix[right] - prefix[left] >= S:
            answer = min(answer, right - left)
            left += 1
        else:
            if right < N:
                right += 1
            else:
                left += 1

    if answer == 100000:
        return 0

    return answer


"""
누적합
prefix[i] 는 nums[i-1] 까지의 합
"""

print(solution3())
