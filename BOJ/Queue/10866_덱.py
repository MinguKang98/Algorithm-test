# 10866_덱
import sys
from collections import deque


class deq:
    def __init__(self) -> None:
        self.d = deque()

    def push_front(self, x: int) -> None:
        self.d.appendleft(x)

    def push_back(self, x: int) -> None:
        self.d.append(x)

    def pop_front(self) -> int:
        if self.empty():
            return -1
        else:
            return self.d.popleft()

    def pop_back(self) -> int:
        if self.empty():
            return -1
        else:
            return self.d.pop()

    def size(self) -> int:
        return len(self.d)

    def empty(self) -> int:
        if self.size():
            return 0
        else:
            return 1

    def front(self) -> int:
        if self.empty():
            return -1
        else:
            return self.d[0]

    def back(self) -> int:
        if self.empty():
            return -1
        else:
            return self.d[-1]


N = int(input())
d = deq()
for _ in range(N):
    command = sys.stdin.readline().rstrip()
    if "push_front" in command:
        _, x = command.split()
        d.push_front(int(x))
    if "push_back" in command:
        _, x = command.split()
        d.push_back(int(x))
    if command == "pop_front":
        print(d.pop_front())
    if command == "pop_back":
        print(d.pop_back())
    if command == "size":
        print(d.size())
    if command == "empty":
        print(d.empty())
    if command == "front":
        print(d.front())
    if command == "back":
        print(d.back())
