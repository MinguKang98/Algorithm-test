# 7568_덩치
import sys


def bigman():
    for i in range(N):
        for j in range(N):
            if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:  # j가 덩치가 클 때
                rank_list[i] += 1


def bigman2():
    for i in arr:
        rank = 1
        for j in arr:
            if i[0] < j[0] and i[1] < j[1]:  # j가 덩치가 클 때
                rank += 1
        print(rank, end=" ")


if __name__ == "__main__":
    N = int(input())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    rank_list = [1] * N
    bigman()
    print(*rank_list)

"""
무엇을 완전탐색 할 것인가?? arr(사람들의 덩치)
"""
