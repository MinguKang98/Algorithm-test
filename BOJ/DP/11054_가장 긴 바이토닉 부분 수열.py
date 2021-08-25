# 11054_가장 긴 바이토닉 부분 수열.py

import sys

# DP
def bitonic(arr, N):
    global num_list
    # arr: i번째 수열의 최대 길이 길이(증가수열 먼저 한 후 감소수열 더함)
    # i번째 증가수열의 최대 길이 길이
    for i in range(1, N):
        for j in range(0, i):
            if num_list[i] > num_list[j] and arr[i] < arr[j] + 1:
                arr[i] = arr[j] + 1

    # i번째 바이토닉 수열의 최대 길이 길이(i번째 감소수열의 최대 길이를 더함)
    for i in range(1, N):
        for j in range(0, i):
            if num_list[i] < num_list[j] and arr[i] < arr[j] + 1:
                arr[i] = arr[j] + 1
    return max(arr)


# DP
def bitonic2(inc_arr, dec_arr, N):
    global num_list
    global reverse_num_list  # reverse된 num_list
    # inc_arr : i번째 증가수열의 최대 길이(주어진 수열 앞부터 계산), dec_arr : i번째 감소수열의 최대 길이(주어진 수열 뒤부터 계산)
    for i in range(1, N):
        for j in range(i):
            if num_list[i] > num_list[j]:
                inc_arr[i] = max(inc_arr[i], inc_arr[j] + 1)
            if reverse_num_list[i] > reverse_num_list[j]:
                dec_arr[i] = max(dec_arr[i], dec_arr[j] + 1)
    # inc_arr와 dec_arr의 합-1의 값들 중 가장 큰 값이 바이토닉 수열의 최대 길이
    result = [0] * N
    for i in range(N):
        result[i] = inc_arr[i] + dec_arr[N - i - 1] - 1
    return max(result)


# 이진탐색 사용 나중에
"""
def lower_bound(left, right, num):
    global arr
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < num:
            # mid 기준 left
            left = mid + 1
        else:
            # mid 기준 right
            right = mid
    return left


def bitonic(N):
    global num_list
    global arr
    max_num=0
    for i in range(1, N):
        for j in range(0, i):
            if num_list[i] > max_num:
                pass
            elif num_list[i] < num_list[i - 1]:
                pass

    return arr[N - 1]
"""
if __name__ == "__main__":
    N = int(input())
    num_list = list(map(int, sys.stdin.readline().split()))
    reverse_num_list = num_list[::-1]
    inc_arr = [1] * N
    dec_arr = [1] * N
    print(bitonic2(inc_arr, dec_arr, N))
