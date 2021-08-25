# 15649_N과 M (1)

import sys
import itertools


def promising(i):
    # 중복되는 숫자가 없다면 promising
    return arr[i] not in arr[1:i]


# BT
def n_m(i):
    global arr, N, M

    if promising(i):
        if i == M:
            for j in range(1, M + 1):
                print(arr[j], end=" ")
            print()
        else:
            for num in range(1, N + 1):
                arr[i + 1] = num
                n_m(i + 1)


# BT
def n_m2(i):
    global arr, N, M

    if i == M:
        print(" ".join((map(str, arr))))
    else:
        for num in range(1, N + 1):
            if num not in arr:  # promising
                arr.append(num)
                n_m2(i + 1)
                arr.pop()


# with permutation
def n_m3():
    global N, M
    P = itertools.permutations(range(1, N + 1), M)  # 1~N까지의 수중 M개를 뽑을때의 조합
    for i in P:
        print(" ".join(map(str, i)))


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    # arr = [0] * (M + 1)
    # arr = []
    n_m3()


"""
1~N 까지 자연수 중 중복없이 M개 고른 수열
"""
