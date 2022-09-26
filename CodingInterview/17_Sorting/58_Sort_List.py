# 58_Sort_List
# https://leetcode.com/problems/sort-list/
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def length(self, root: ListNode) -> int:
        length, node = 0, root
        while node:
            length += 1
            node = node.next
        return length

    def print(self, root):
        node = root
        while node:
            print(node.val, end=' ')
            node = node.next
        print()

    def mergeList(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 and list2:
            if list1.val > list2.val:
                list1, list2 = list2, list1
            list1.next = self.mergeList(list1.next, list2)
        return list1 or list2  # return list1. if list1 is None, return list2

    """
    list1 을 항상 작은 리스트로 설정 => list1이 더 큰 경우는 swap
    list1.next 는 list1.next와 list2의 mergeList 로 설정
    """

    # Solution0 - using merge sort
    def sortList0(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        n = self.length(head)
        mid = n // 2
        left = head
        for i in range(mid - 1):
            left = left.next
        right, left.next = left.next, None

        left_list = self.sortList(head)
        right_list = self.sortList(right)

        return self.mergeList(left_list, right_list)

    """
    연결리스트를 분할하기 위해 리스트의 길이를 사용 -> 리스트 길이 나타내는 함수 구현
    분활 후 mergeList 
    """

    # Solution1 - using merge sort & runner
    def sortList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head

        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None

        list1 = self.sortList1(head)
        list2 = self.sortList1(slow)

        return self.mergeList(list1, list2)

    """
    연결리스트를 분할하기 위해 runner 기법을 사용
    runner 기법은 연결리스트 탐색 시 사용되는 기법이다. 한 칸씩 가는 slow와 두 칸씩 가는 fast를 설정하여
    fast가 맨 끝에 도착하면 slow는 중앙에 도착하므로 연결리스트의 중간 위치를 빠르게 알 수 있다. 
    분활 후 mergeList 
    runner 기법 사용으로 Solution0 보다 빠른 속도
    """

    # Solution2 - using built-in sort
    def sortList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        lst: List = []
        while node:
            lst.append(node.val)
            node = node.next

        lst.sort()

        node = head
        for i in range(len(lst)):
            node.val = lst[i]
            node = node.next
        return head

node1 = ListNode(4)
node2 = ListNode(2)
node3 = ListNode(1)
node4 = ListNode(3)
node1.next, node2.next, node3.next = node2, node3, node4
Solution().sortList(node1)
