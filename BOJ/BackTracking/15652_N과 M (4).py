# 15652_N과 M (4)
import itertools


def promising(num):
    if len(arr) == 0:
        return True
    else:
        return arr[-1] <= num


# BT
def n_m(i):
    if i == M:
        print(" ".join(map(str, arr)))
    else:
        for num in range(1, N + 1):
            if promising(num):
                arr.append(num)
                n_m(i + 1)
                arr.pop()


# with combination_wtih_replacement
def n_m2():
    print(
        "\n".join(
            map(
                " ".join,
                itertools.combinations_with_replacement(map(str, range(1, N + 1)), M),
            )
        )
    )


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = []
    n_m2()
