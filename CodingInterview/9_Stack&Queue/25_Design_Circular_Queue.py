# 25_Design_Circular_Queue

# Solutino0 - my solution
class MyCircularQueue0:
    def __init__(self, k: int):
        self.queue = [-1] * k
        self.max_length = k
        self.front_idx = 0
        self.rear_idx = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            if self.isEmpty():
                self.queue[self.rear_idx] = value
            else:
                self.rear_idx = (self.rear_idx + 1) % self.max_length
                self.queue[self.rear_idx] = value
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            if self.front_idx == self.rear_idx:
                self.queue[self.front_idx] = -1
            else:
                self.queue[self.front_idx] = -1
                self.front_idx = (self.front_idx + 1) % self.max_length
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front_idx]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear_idx]

    def isEmpty(self) -> bool:
        return self.front_idx == self.rear_idx and self.queue[self.front_idx] == -1

    def isFull(self) -> bool:
        for i in range(self.max_length):
            if self.queue[i] == -1:
                return False
        return True

    """
    모든 idx의 위치가 현재 값의 idx로 표현
    isFull 연산이 loop 연산이 있어 비효율적
    """


# Solutino1 - book answer
class MyCircularQueue1:
    def __init__(self, k: int):
        self.queue = [None] * k
        self.max_length = k
        self.front_idx = 0
        self.rear_idx = 0

    def enQueue(self, value: int) -> bool:
        if self.queue[self.rear_idx] is None:
            self.queue[self.rear_idx] = value
            self.rear_idx = (self.rear_idx + 1) % self.max_length
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.queue[self.front_idx] is None:
            return False
        else:
            self.queue[self.front_idx] = None
            self.front_idx = (self.front_idx + 1) % self.max_length
            return True

    def Front(self) -> int:
        return -1 if self.queue[self.front_idx] is None else self.queue[self.front_idx]

    def Rear(self) -> int:
        return (
            -1
            if self.queue[self.rear_idx - 1] is None
            else self.queue[self.rear_idx - 1]
        )

    def isEmpty(self) -> bool:
        return self.front_idx == self.rear_idx and self.queue[self.front_idx] is None

    def isFull(self) -> bool:
        return (
            self.front_idx == self.rear_idx and self.queue[self.front_idx] is not None
        )

    """
    front의 idx = 현재 idx but, rear의 idx = 다음 값의 idx로 표현
    isFull의 코드가 단순해짐
    """
