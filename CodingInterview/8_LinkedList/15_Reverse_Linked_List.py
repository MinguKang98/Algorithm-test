# 15_Reverse_Linked_List
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution0 - Fail
def reverseList0(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        head = head.next
    else:
        head, head.next = reverseList0(head.next), head
    return head


# Solution1 - Rercursion
def reverseList1(head: Optional[ListNode]) -> Optional[ListNode]:
    def reverse_list(node: ListNode, prev: ListNode = None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse_list(next, node)

    return reverse_list(head)


"""
next - 다음 노드 node - 현재 노드
node에 None이 올때까지 node.next에 prev를 연결하며 재귀호출
"""

# Solution2 - iterative
def reverseList2(head: Optional[ListNode]) -> Optional[ListNode]:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        node, prev = next, node

    return prev


"""
알고리즘은 거의 유사
하지만 반복이 재귀에 비해 낮은 공간 복잡도를 가지고 시행 속도 또한 빠름
"""
