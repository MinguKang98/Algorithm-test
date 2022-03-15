# 24_Implement_Queue_using_Stacks

# Solution0 - my solution
class MyQueue0:
    def __init__(self):
        self.s = []
        self.temp = []

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        while self.s:
            self.temp.append(self.s.pop())
        result = self.temp.pop()
        while self.temp:
            self.s.append(self.temp.pop())
        return result

    def peek(self) -> int:
        while self.s:
            self.temp.append(self.s.pop())
        result = self.temp[-1]
        while self.temp:
            self.s.append(self.temp.pop())
        return result

    def empty(self) -> bool:
        return len(self.s) == 0


"""
항상 pop과 peek 수행시 항상 stack의 방향 뒤집어 놓음
"""

# Solution1 -
class MyQueue1:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()  # output이 비어있다면 output으로 옮겨줌
        return self.output.pop()

    def peek(self) -> int:
        if not self.output:  # output이 비어있다면 output으로 값들 이동 -> ouput의 top==head
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return self.input == [] and self.output == []


"""
output이 비었을때 input의 값들을 output으로 이동-> output의 top == head 유지
input에 값들이 쌓여도 output 비어있을때까지는 유지 -> output 값들이 빈다면 다시 input 값 이동
매번 stack의 방향 뒤집지 않아도 됨
"""
