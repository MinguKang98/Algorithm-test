# 15651_N과 M (3)

import itertools

# BT
def n_m(i):
    global arr, N, M
    if i == M:
        print(" ".join(map(str, arr)))
    else:
        for num in range(1, N + 1):
            arr.append(num)
            n_m(i + 1)
            arr.pop()


# with product
def n_m2():
    global N, M
    print(
        "\n".join(map(" ".join, itertools.product(map(str, range(1, N + 1)), repeat=M)))
    )


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = []
    n_m2()
