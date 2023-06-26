# 10830_행렬_제곱_Gold4
# https://www.acmicpc.net/problem/10830


N, B = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))


def matrix_prod(matrix1, matrix2):
    temp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                temp[i][j] += matrix1[i][k] * matrix2[k][j]
            temp[i][j] %= 1000
    return temp


def matrix_prod2(matrix1, matrix2):
    temp = [[0 for _ in range(len(matrix1))] for _ in range(len(matrix2[0]))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix1[0])):
                temp[i][j] += matrix1[i][k] * matrix2[k][j]
            temp[i][j] %= 1000
    return temp


"""
정사각행렬 아닐 경우도 고려한 행렬의 곱
matrix1 이 p*q,  matrix2 이 q*r 라 하자
그렇다면 len(matrix1) = p, len(matrix1[0]) = len(matrix2) = q, len(matrix2[0]) = r
"""


def matrix_pow(matrix, n):
    if n == 1:
        for i in range(N):
            for j in range(N):
                matrix[i][j] %= 1000
        return matrix
    elif n % 2 == 0:
        temp = matrix_pow(matrix, n // 2)
        return matrix_prod2(temp, temp)
    else:
        temp = matrix_pow(matrix, n - 1)
        return matrix_prod2(temp, matrix)


answer = matrix_pow(matrix, B)
for a in answer:
    print(*a)

"""
직접 거듭제곱 계산 -> O(n^3) 이상 나오는 듯해 패스
제곱을 계산해서?? 홀수제곱은 A^(n-1) * A, 짝수제곱은 (A^(n//2))^2 => 아이디어는 맞음 

행렬 곱셈을 코딩으로 처음 접해서 서칭으로 해결
행렬의 곱셈 코드 알아두자

해당 문제는 Divide&Conquer 유형
n 이 홀수, 짝수 일때 divide 하여 부분 문제로 바꿈        ex) temp = matrix_pow(matrix, n // 2)
부분 문제들을 condquer 한 후 통합한다.                  ex) return matrix_prod2(temp, temp)
"""
