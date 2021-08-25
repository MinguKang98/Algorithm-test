# 15650_N과 M (2)


def promising(num):
    # 중복 없고 오름차순
    global arr
    if len(arr) == 0:
        return True
    else:
        return num not in arr and arr[-1] < num


def n_m(i):
    global arr, N, M
    if i == M:
        print(" ".join(map(str, arr)))
    else:
        for num in range(1, N + 1):
            if promising(num):
                arr.append(num)
                n_m(i + 1)
                arr.pop()


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = []
    n_m(0)
