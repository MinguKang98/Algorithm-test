# 13_Palindrome_Linked_List
from collections import deque
from typing import Deque, Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# solution1 - List
def isPalindrome1(head: Optional[ListNode]) -> bool:
    temp_list: List = []

    if not head:
        return True

    node = head

    # ListNode 를 list로 변환
    while node is not None:
        temp_list.append(node.val)
        node = node.next

    while len(temp_list) > 1:  # list의 길이가 1이여도 Palindrome
        if temp_list.pop(0) != temp_list.pop():  # 앞과 뒤가 다르면 False
            return False
    return True  # 모두 같으므로 True


"""
pop(0)의 시간복잡도는 O(n) - 모든 값이 한칸씩 이동하므로
"""

# solution2 - Deque
def isPalindrome2(head: Optional[ListNode]) -> bool:
    temp_deque: Deque = deque()

    if not head:
        return True

    node = head

    # ListNode 를 Deque로 변환
    while node is not None:
        temp_deque.append(node.val)
        node = node.next

    while len(temp_deque) > 1:  # Dequq의 길이가 1이여도 Palindrome
        if temp_deque.popleft() != temp_deque.pop():  # 앞과 뒤가 다르면 False
            return False
    return True  # 모두 같으므로 True


"""
popleft()의 시간복잡도는 O(1)
따라서 sol1보다 빠름
"""

# solution3 - Runner
def isPalindrome3(head: Optional[ListNode]) -> bool:
    rev = None
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next  # fast는 두칸씩
        rev, rev.next, slow = slow, rev, slow.next  # rev는 slow의 역순으로 생성

    if fast:  # 노드 개수 홀수일때 중앙값 건너뜀
        slow = slow.next

    while rev and rev.val == slow.val:  # Palindrome 여부 확인
        slow, rev = slow.next, rev.next

    return not rev  # rev에 노드 없으면 True, 남으면 False


"""
runner 기법 사용
-> 연결리스트 순회 시 2개의 포인터 동시 사용하는 기법
    한 포인터가 다른 포인터 앞서게 하여 여러 수치 판별
"""
