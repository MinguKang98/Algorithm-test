# 60_Insertion_Sort_List
# https://leetcode.com/problems/insertion-sort-list/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Solution0 - using insertion sort
    def insertionSortList0(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()

        node = head
        while node:
            temp = root
            while temp:
                if not temp.next or node.val < temp.next.val:
                    temp.next, temp.next.next = ListNode(node.val), temp.next
                    break
                temp = temp.next
            node = node.next

        return root.next

    """
    앞으로 돌아오는 거 어떻게? 기존 노드 사용하면 이전 노드 확인 힘듬 => 새 노드 생성 후 insert
    temp.next 가 None 이거나 현재 노드의 val이 temp.next.val 보다 작으면 temp.next 에
    노드를 생성하여 삽입한다.
    O(n^2) 의 시간 복잡도
    """

    # Solution1 - using insertion sort
    def insertionSortList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = parent = ListNode(None)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            cur.next, head, cur.next.next = head, head.next, cur.next
            # cur.next, head.next, head = head, cur.next, head.next - 이 방식도 가능(정답지)
            cur = parent

        return cur.next

    """
    정렬할 대상과 정렬을 끝낸 대상으로 나눈다.
    cur은 정렬 끝낸 대상, head는 정렬 대상, parent는 루트를 가리킨다.
    cur.next 가 존재하고 cur.next.val < head.val 이면 cur 을 이동
    아니라면 값을 삽입한다.
    """

    # Solution2 - using insertion sort with optimization
    def insertionSortList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = parent = ListNode(0)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next

            if head and head.val < cur.val:  # 필요한 경우만 cur 이 되돌아감
                cur = parent

        return parent.next

    """
    head.val 이 cur.val 보다 작을때 만 돌아가면 됨
    즉, 넣을 값이 현재 값보다 작을 때만 cur 이 되돌아가면 된다.
    최적화 되어 Solution0, 1보다 10배 이상 빠른 속도
    """
