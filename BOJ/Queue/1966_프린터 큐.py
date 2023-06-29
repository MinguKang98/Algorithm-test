# 1966_프린터 큐
import sys
from typing import List
from collections import deque

# 처음 코드
def printQ0(N: int, M: int, P: List[int]) -> int:
    cnt = 0
    q = deque(P)  # 중요도 큐
    idx = deque(list(range(N)))  # index 큐
    while M in idx:  # M번째가 없기 전까지
        if q[0] < max(q):  # 중요도 높은거 뒤에
            q.append(q.popleft())
            idx.append(idx.popleft())
        else:  # 아니면 print
            q.popleft()
            idx.popleft()
            cnt += 1
    return cnt


# rotate 함수 - 좀 더 빠름
def printQ1(N: int, M: int, P: List[int]) -> int:
    cnt = 0
    q = deque(P)  # 중요도 큐
    idx = deque(list(range(N)))  # index 큐
    while M in idx:  # M번째가 없기 전까지
        if q[0] < max(q):  # 중요도 높은거 뒤에
            q.rotate(-1)
            idx.rotate(-1)
        else:  # 아니면 print
            q.popleft()
            idx.popleft()
            cnt += 1
    return cnt


# list 사용
def printQ2(N: int, M: int, P: List[int]) -> int:
    cnt = 0
    idx = [0 for _ in range(N)]  # index 큐
    idx[M] = 1
    while True:  # M번째가 없기 전까지
        if P[0] == max(P):  # 중요도 높은거 뒤에
            cnt += 1
            if idx[0] != 1:
                del P[0]
                del idx[0]
            else:
                return cnt

        else:  # 아니면 print
            P.append(P[0])
            idx.append(idx[0])
            del P[0]
            del idx[0]


T = int(input())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    P = list(map(int, sys.stdin.readline().split()))
    print(printQ2(N, M, P))

"""
N개의 문서
중요도 높은 문서 뒤에 있으면 큐 맨뒤에 배치
아니면 인쇄
M번째 문서는 언제 인쇄??
"""
