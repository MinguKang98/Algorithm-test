# 16_Add_Two_Numbers
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            node, prev = next, node

        return prev

    def ListNodeToList(self, head: Optional[ListNode]) -> List:
        result: List = []
        node = head

        while node:
            result.append(node.val)
            node = node.next
        return result

    def StrToReversedListNode(self, nums: str) -> Optional[ListNode]:
        prev: ListNode = None

        for num in nums:
            node = ListNode(num)
            node.next = prev
            prev = node
        return node

    # Solution1 - Type Convert
    def addTwoNumbers1(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        list1 = self.ListNodeToList(self.reverseList(l1))
        list2 = self.ListNodeToList(self.reverseList(l2))
        # 더해
        result = int("".join(str(e) for e in list1))
        +int("".join(str(e) for e in list2))
        resultNode = self.StrToReversedListNode(str(result))
        return resultNode

    """
    ListNode를 reverse
    ListNode -> List
    덧셈 계산 
    int -> str -> ListNode
    """

    # Solution2 - Full Adder
    def addTwoNumbers2(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        root = head = ListNode(0)

        q = 0  # 올리는 수
        while l1 or l2 or q:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next

            if l2:
                sum += l2.val
                l2 = l2.next

            q, r = divmod(sum + q, 10)  # 몫과 나머지 - 올리는 수 & 해당 자리 수
            head.next = ListNode(r)
            head = head.next

        return root.next


"""
시간 차이는 별로 없으나 2번째 코드가 좀 더 깔끔
"""
