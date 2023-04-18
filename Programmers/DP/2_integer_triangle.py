# 2_integer_triangle
# https://school.programmers.co.kr/learn/courses/30/lessons/43105

def solution0(triangle):
    sub_sums = [[-1 for _ in range(i + 1)] for i in range(len(triangle))]
    sub_sums[0][0] = triangle[0][0]

    for i, sums in enumerate(sub_sums[:-1]):
        for j in range(len(sums)):
            sub_sums[i + 1][j] = max(sub_sums[i + 1][j], sub_sums[i][j] + triangle[i + 1][j])
            sub_sums[i + 1][j + 1] = max(sub_sums[i + 1][j + 1], sub_sums[i][j] + triangle[i + 1][j + 1])

    return max(sub_sums[-1])


"""
(i,j) 에서 왼쪽 아래는 (i+1, j) 오른쪽 아래는 (i+1, j+1)
다른 방향에서 오는 합은 둘 중 큰것만 저장해도 ㄱㅊ
(0,0) 에서 아래로 내려가며 합을 구함
타뷸레이션을 사용해 합을 저장해가며 풀이
"""


def solution1(triangle):
    memo = {}

    def f(triangle, i, j, memo):
        if i == len(triangle) - 1:  # 마지막 행이면 return
            return triangle[i][j]

        if (i, j) in memo:  # 이미 계산한 것이면 return
            return memo[(i, j)]

        left = f(triangle, i + 1, j, memo)
        right = f(triangle, i + 1, j + 1, memo)
        x = triangle[i][j] + max(left, right)

        memo[(i, j)] = x
        return x  # 현재 위치까지의 합

    return f(triangle, 0, 0, memo)


"""
마지막 행에서 위로 올라가며 합을 구함
재귀를 사용한 메모이제이션 방식
현재 위치의 왼쪽 아래의 합(left)과 오른쪽 아래의 합(right) 중 큰 값을 선택에 현재 값(triangle[i][j])에 더함
"""

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

print(solution1(triangle))
