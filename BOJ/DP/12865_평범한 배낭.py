# 12865_평범한 배낭.py

import sys

# DP 1-dimension list
def kanpsack(weight_list, value_list, N, K):
    # arr[j] : weight가 j일때 max value
    global arr

    for i in range(1, N + 1):
        for j in range(K, 0, -1):
            if weight_list[i] <= j:
                arr[j] = max(arr[j], arr[j - weight_list[i]] + value_list[i])
    return arr[K]


# DP 2-dimension list
def kanpsack2(weight_list, value_list, N, K):
    # arr[i][j] : i번째 item까지만 choose 할 때 weigth가 j이하의 max value
    global arr

    for i in range(1, N + 1):
        for j in range(1, K + 1):
            # i번째 item의 weight가 j보다 작거나 같다면 추가
            if weight_list[i] <= j:
                arr[i][j] = max(
                    arr[i - 1][j], arr[i - 1][j - weight_list[i]] + value_list[i]
                )
            # 크다면 이전 것
            else:
                arr[i][j] = arr[i - 1][j]
    return arr[N][K]


if __name__ == "__main__":
    # N : 개수 K : 무게
    N, K = map(int, sys.stdin.readline().split())
    arr = [0] * (K + 1)
    # arr = [[0] * (K + 1) for _ in range(N + 1)]
    weight_list = [0] * (K + 1)
    value_list = [0] * (K + 1)
    for i in range(1, N + 1):
        weight_list[i], value_list[i] = map(int, sys.stdin.readline().split())
    print(kanpsack(weight_list, value_list, N, K))


"""
가치의 최댓값
arr[i] 은 weigth 가 i일때  max value


"""
