# 17_Swap_Nodes_in_Pairs
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Solution0 - my code
    def swapPairs0(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(0)
        root.next = head

        while head:
            if head.next == None:
                break
            head.val, head.next.val = head.next.val, head.val
            head = head.next.next

        return root.next

    # Solution1 - change value
    def swapPairs1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next

        return head

    # Solutino2 - change iterative
    def swapPairs2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            # change node
            temp_node = head.next
            head.next = temp_node.next
            temp_node.next = head

            prev.next = temp_node

            # move node
            head = head.next  # node 교환 시 head의 위치도 변경되었으므로 한칸만 이동함
            prev = prev.next.next

        return root.next

    # Solutino3 - change recursive
    def swapPairs3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:  # 교환 가능 일 경우
            temp_node = head.next
            head.next = self.swapPairs3(temp_node.next)  # 모르는 뒷부분은 재귀 함수에 넘겨 받음
            temp_node.next = head
            return temp_node
        return head  # head만 있거나 없다면 바로 return
