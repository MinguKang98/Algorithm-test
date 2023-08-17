# 2805_나무_자르기_Silver2
# https://www.acmicpc.net/problem/2805

N, M = map(int, input().split())
heights = list(map(int, input().split()))


def solution0():
    left = 1
    right = max(heights)

    answer = 0
    while left <= right:
        mid = (left + right) // 2
        temp = 0
        for height in heights:
            if height > mid:
                temp += height - mid

        # if M < temp: 
        #     left = mid + 1
        # else:
        #     right = mid - 1
        #     answer = mid
        # 오답

        if M > temp:
            right = mid - 1
        else:
            left = mid + 1
            answer = mid

    return answer


"""
높이를 H 로 설정하면 나무에서 H 만큼 남기고 잘라냄. H 보다 작으면 안잘림
H는 나무 높이의 최소와 최대 사이의 어딘가 (최악의 경우 1 ~ 1,000,000,000)
이진탐색 써야하는 이유? H 는 자연수 범위 사이의 어느 값인데 1씩 증가하며 탐색하기엔 불가
=> 이진탐색으로...

처음 오답
=> if M > temp 관련 순서 바꾸니 정답
why?? 나무의 합은 M 보다 크거나 같아도 되므로 해당 시점에서 answer 을 초기화해야한다.
"""


def solution1():
    left = 1
    right = max(heights)

    while left <= right:
        mid = (left + right) // 2
        temp = 0
        for height in heights:
            if height > mid:
                temp += height - mid

        if M > temp:
            right = mid - 1
        else:
            left = mid + 1

    return right


"""
answer 초기화 하지 말고 right 가 최종 정답으로 
"""

print(solution1())
