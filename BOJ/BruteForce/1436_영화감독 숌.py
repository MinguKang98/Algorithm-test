# 1436_영화감독 숌
import sys


def num_end(N):
    cnt = 0
    for num in range(666, sys.maxsize):
        if "666" in str(num):  # 666이 들어감
            cnt += 1
            if cnt == N:
                return num


# while 사용한게 더 오래걸림
def num_end2(N):
    cnt = 0
    num = 666
    while True:
        if "666" in str(num):  # 666이 들어감
            cnt += 1
            if cnt == N:
                return num
        num += 1


if __name__ == "__main__":
    N = int(input())  # N<=10000
    print(num_end2(N))


"""
무엇을 완전탐색?? 숫자를 N까지
어떤 조건에 count?? 숫자에 666이 들어갈 때 
"""
