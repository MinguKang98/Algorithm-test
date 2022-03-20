# 26_Design_Circular_Deque


class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyCircularDeque:
    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.len, self.max_len = 0, k
        self.head.next, self.tail.prev = self.tail, self.head

    # 최적화를 위한 코드
    def add_node(self, cur_node: ListNode, value: int):
        temp_node = cur_node.next
        new_node = ListNode(value, cur_node, temp_node)
        cur_node.next, temp_node.prev = new_node, new_node

    def del_node(self, cur_node: ListNode):
        temp_node = cur_node.next.next
        cur_node.next, temp_node.prev = temp_node, cur_node

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            """
            new_node = ListNode(value, self.head, self.head.next)
            self.head.next, self.head.next.prev = new_node, new_node

            같은 알고리즘으로 짠 코드지만 위의 코드는 다른 결과를 반환
            WHY? self.head.next.prev는 값이 변할 수 있으므로 self.head.next를
            새로운 변수로 할당하고 그 변수의 prev를 쓰는 것이 정확한 코드인 것 같음
            """

            # temp_node = self.head.next
            # new_node = ListNode(value, self.head, temp_node)
            # self.head.next, temp_node.prev = new_node, new_node
            self.add_node(self.head, value)  # 최적화

            self.len += 1
            return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            # temp_node = self.tail.prev
            # new_node = ListNode(value, temp_node, self.tail)
            # self.tail.prev, temp_node.next = new_node, new_node
            self.add_node(self.tail.prev, value)  # 최적화

            self.len += 1
            return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.len -= 1
            # temp_node = self.head.next.next
            # self.head.next, temp_node.prev = temp_node, self.head
            self.del_node(self.head)  # 최적화

            return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.len -= 1
            # temp_node = self.tail.prev.prev
            # self.tail.prev, temp_node.next = temp_node, self.tail
            self.del_node(self.tail.prev.prev)  # 최적화

            return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.head.next.val

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.tail.prev.val

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.max_len


deq = MyCircularDeque(3)
print(deq.insertLast(1))
print(deq.insertLast(2))
print(deq.insertFront(3))
print(deq.insertFront(4))
print(deq.getRear())
print(deq.isFull())
print(deq.deleteLast())
print(deq.insertFront(4))
print(deq.getFront())
