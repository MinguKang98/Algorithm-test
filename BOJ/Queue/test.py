# 5430_AC
import sys
from collections import deque
from typing import List

# input = sys.stdin.readline().rstrip()


def AC(p: str, n: int, num_list: List[int]) -> None:
    q = deque(num_list)
    for command in p:
        if command == "R":
            q.reverse()
        if command == "D":
            if len(q) == 0:
                print("error")
                return
            else:
                q.popleft()
    print("[" + ",".join(map(str, q)) + "]")


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    p = str(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    num_list = list(
        map(int, sys.stdin.readline().rstrip()[1:-1].replace(",", " ").split())
    )
    AC(p, n, num_list)

"""
1
RDD
4
[1,2,3,4]

R - reverse
d - popleft
if use D when empty -> error
"""
