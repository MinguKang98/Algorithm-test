# 18_Odd_Even_Linked_List
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Solution0 - my code
    def oddEvenList0(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ord_head = head
        temp_root = temp_head = ListNode(None)

        while ord_head and ord_head.next:
            even_head = ord_head.next
            ord_head.next = even_head.next
            even_head.next = None
            temp_head.next = even_head

            ord_head = ord_head.next
            temp_head = temp_head.next

        ord_head.next = temp_root.next
        return head

    """
    예시는 통과하나 코트 에러 나옴
    """

    # Solutino1 - change iterative
    def oddEvenList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        odd = head
        even_head = even = head.next

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        odd.next = even_head
        return head

    """
    공간복잡도 O(1), 시간복잡도 O(n)을 요구했으므로 연결리스트를 리스트로 변경하는 방법 불가
    """
