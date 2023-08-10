# 2138_전구와_스위치_Gold5
# https://www.acmicpc.net/problem/2138
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
before = list(map(int, list(input().rstrip())))
after = list(map(int, list(input().rstrip())))

result = -1


def solution0():
    def dfs(bulbs, depth):
        global result

        if bulbs == after:
            result = depth
            return

        if depth >= N:
            return

        if depth < 2:
            dfs(bulbs, depth + 1)

            for i in (-1, 0, 1):
                temp = depth + i
                if 0 <= temp < N:
                    bulbs[temp] ^= 1
            dfs(bulbs, depth + 1)
            for i in (-1, 0, 1):
                temp = depth + i
                if 0 <= temp < N:
                    bulbs[temp] ^= 1
        else:
            if bulbs[depth - 2] == after[depth - 2]:
                dfs(bulbs, depth + 1)

                for i in (-1, 0, 1):
                    temp = depth + i
                    if 0 <= temp < N:
                        bulbs[temp] ^= 1
                dfs(bulbs, depth + 1)
                for i in (-1, 0, 1):
                    temp = depth + i
                    if 0 <= temp < N:
                        bulbs[temp] ^= 1

    dfs(before, 0)
    return result


"""
i -> i-1, i, i+1 변화
before -> after 되는데 최소값

000 -> 010
1, 2, 3 누르면 됨 (순서 상관 ㄴ)
스위치는 한번 누르거나 안 눌러야 함 -> 짝수 번은 0번, 홀수 번은 1번과 같음
bfs +가지치ㅣ기?
글자 변경 이슈로 백트래킹으로..

시간초과
"""


def solution1():
    before2 = before[:]
    before2[0] ^= 1
    before2[1] ^= 1

    result1, result2 = 0, 1
    for i in range(1, N):
        prev1, prev2 = before[i - 1], before2[i - 1]

        if prev1 != after[i - 1]:
            for j in (-1, 0, 1):
                temp = i + j
                if 0 <= temp < N:
                    before[temp] ^= 1
            result1 += 1

        if prev2 != after[i - 1]:
            for j in (-1, 0, 1):
                temp = i + j
                if 0 <= temp < N:
                    before2[temp] ^= 1
            result2 += 1

    if before != after:
        result1 = sys.maxsize
    if before2 != after:
        result2 = sys.maxsize

    answer = min(result1, result2)
    if answer == sys.maxsize:
        return -1
    return answer


"""
정답 보고 아이디어 => index 1 부터 before[i-1] 값이 after[i-1] 값과 다르면 변경
이때 index 0, 1 의 값을 바꿨을 때, 안 바꿨을 때 구분해서 가야함.
즉, 1번 스위치 눌렀을 때, 안 눌렀을 때 구분
"""


def solution2():
    def change(A, B):
        A_copy = A[:]
        press = 0
        for i in range(1, N):

            if A_copy[i - 1] == B[i - 1]:
                continue

            press += 1
            for j in range(i - 1, i + 2):
                if j < N:
                    A_copy[j] = 1 - A_copy[j]
        if A_copy == B:
            return press
        else:
            return sys.maxsize

    answer = change(before, after)
    before[0] ^= 1
    before[1] ^= 1
    answer = min(answer, change(before, after) + 1)
    if answer != sys.maxsize:
        return answer
    return -1


"""
solution1 과 같은 풀이방법이지만 다른 표현법.
유사 동작 메서드로 묶음, xor 대신 1 - X 사용
"""

print(solution1())
