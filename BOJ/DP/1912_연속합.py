# 1912_연속합.py

import sys


def consec_sum(num_list, N):
    global arr

    for i in range(N):
        # arr[i]는 num_list[i]와 arr[i-1]+num_list[i] 중 최대값으로 정의
        arr[i] = max(num_list[i], arr[i - 1] + num_list[i])
    return max(arr)


if __name__ == "__main__":
    N = int(input())
    num_list = list(map(int, sys.stdin.readline().split()))
    arr = [0] * N
    print(consec_sum(num_list, N))

"""
가장 큰 연속합을 구하여라

arr[i] : i를 포함하는 연속합의 최대

***무엇을 메모이제이션 할 것인가(정의내리기)

"""
