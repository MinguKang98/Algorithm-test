# 11866_요세푸스 문제 0
import sys
from collections import deque

# 기존 코드
def josephus0(N:int,K:int) -> None:
    q=deque(list(range(1,N+1)))
    result=[]
    while len(q)>0:
        for i in range(K-1):
            q.append(q.popleft())
        result.append(str(q.popleft()))
    res=", ".join(result)
    print("<"+res+">")

# dequeue의 rotate 함수 사용
def josephus1(N:int,K:int) -> None:
    q=deque(list(range(1,N+1)))
    result=[]
    while len(q)>0:
        q.rotate(-(K-1))
        result.append(str(q.popleft()))
    res=", ".join(result)
    print("<"+res+">")

N,K=map(int,sys.stdin.readline().split())
josephus1(N,K)
