# 1080_행렬_Silver1
# https://www.acmicpc.net/problem/1080

N, M = map(int, input().split())
matrix1 = [list(map(int, list(input()))) for _ in range(N)]
matrix2 = [list(map(int, list(input()))) for _ in range(N)]


def solution0():
    if (N < 3 or M < 3) and matrix1 != matrix2:
        return -1

    result = 0
    for i in range(N - 2):
        for j in range(M - 2):
            if matrix1[i][j] != matrix2[i][j]:
                result += 1
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        matrix1[x][y] ^= 1

    if matrix1 != matrix2:
        return -1
    return result


"""
행렬 변환 : 3x3 부분행렬 모든 원소 전환
3x3 으로 순회하며 다르면 그냥 전환하기? => 풀이방법 맞음
오답이여서 이유 확인 => 예외처리가 덜됨
=> N < 3 or M < 3 만 예외 처리했는데 N < 3 or M < 3 이면서 matrix1 != matrix2 을
만족해야함. matrix1 == matrix2 이라면 바꾸지 않아도 되어 답이 0이 되기 때문

3x3 으로 순회하며 다르면 그냥 전환 => 그리디
"""

print(solution0())
