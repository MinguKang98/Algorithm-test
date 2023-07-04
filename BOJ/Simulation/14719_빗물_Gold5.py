# 14719_빗물_Gold5
# https://www.acmicpc.net/problem/14719

H, W = map(int, input().split())
blocks = list(map(int, input().split()))


def solution1():
    answer = 0
    for idx in range(1, W - 1):
        left_max = max(blocks[:idx])
        right_max = max(blocks[idx + 1:])

        temp = min(left_max, right_max)

        if temp > blocks[idx]:
            answer += temp - blocks[idx]

    return answer


"""
올라가기만 or 내려가기만 하면 빗물 안고임
내려갔다 올라가야 고임 => 이걸 어케 판단??

풀이 참고 => 왼쪽 최대와 오른쪽 최대 중 작은 값을 기준으로 현재 값과 비교
이때 탐색 값들중 처음과 마지막 값은 물이 고이지 않으므로 제외
"""


def solution2():
    answer = 0
    left, right = 0, len(blocks) - 1
    left_max, right_max = blocks[left], blocks[right]

    while left < right:
        left_max = max(left_max, blocks[left])
        right_max = max(right_max, blocks[right])

        if left_max < right_max:
            answer += left_max - blocks[left]
            left += 1
        else:
            answer += right_max - blocks[right]
            right -= 1

    return answer


"""
solution1 과 비슷하지만 투포인터를 사용한 풀이
왼쪽의 최댓값과 오른쪽의 최댓값을 구한 후, 작은 것을 기준으로 고인 양을 구하고
인덱스를 옮긴다
"""

print(solution2())
