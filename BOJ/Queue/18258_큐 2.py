# 18258_큐 2
import sys
from collections import deque


class queue2:
    def __init__(self) -> None:
        self.q = deque()

    def push(self, num: int) -> None:
        self.q.appendleft(num)

    def pop(self) -> int:
        if self.empty():
            return -1
        else:
            return self.q.pop()

    def size(self) -> int:
        return len(self.q)

    def empty(self) -> int:
        if self.size():
            return 0
        else:
            return 1

    def front(self) -> int:
        if self.empty():
            return -1
        else:
            return self.q[-1]

    def back(self) -> int:
        if self.empty():
            return -1
        else:
            return self.q[0]


N = int(input())
q = queue2()
for i in range(N):
    command = sys.stdin.readline().rstrip()
    if "push" in command:
        _, num = command.split()
        q.push(int(num))
    if command == "pop":
        print(q.pop())
    if command == "size":
        print(q.size())
    if command == "empty":
        print(q.empty())
    if command == "front":
        print(q.front())
    if command == "back":
        print(q.back())
