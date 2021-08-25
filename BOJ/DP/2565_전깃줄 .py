# 2565_전깃줄 .py

import sys

# DP
def min_elec(elec_list, N):
    global arr
    for i in range(N):
        for j in range(i):
            if elec_list[i][1] > elec_list[j][1]:
                arr[i] = max(arr[i], arr[j] + 1)
    return N - max(arr)


if __name__ == "__main__":
    N = int(input())
    arr = [1] * N
    elec_list = []
    for i in range(N):
        elec_list.append(list(map(int, sys.stdin.readline().split())))
    elec_list.sort()
    print(min_elec(elec_list, N))

"""
풀이방법
전깃줄을 최소로 제거하여 B전봇대 위치의 순서가 오름차순이 되게 만들어라
-> B전봇대의 위치의 순서가 오름차순이 되는 전깃줄의 최대 갯수
"""
