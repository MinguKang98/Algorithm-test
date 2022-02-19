# 19_Reverse_Linked_List2
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        # 예외처리
        if not head or left == right:
            return head

        # start end 세팅 - left 전 위치가 start, left 위치가 end
        # list가 변경되어도 둘의 index는 변하지 않음
        root = start = ListNode(None)
        root.next = head
        for _ in range(left - 1):
            start = start.next
        end = start.next

        # reverse List
        for _ in range(right - left):
            temp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = temp

        return root.next
