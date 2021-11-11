# 2164_카드2
from collections import deque

def card(N:int) -> int:
    q=deque(list(range(1,N+1)))
    while len(q)!=1:
        q.popleft()
        q.append(q.popleft())
    return q[0]

N=int(input())
print(card(N))