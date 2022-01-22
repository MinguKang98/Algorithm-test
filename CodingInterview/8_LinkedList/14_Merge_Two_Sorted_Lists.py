# 14_Merge_Two_Sorted_Lists
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution1 - Recursion
def mergeTwoLists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    if (not list1) or (
        list2 and list1.val > list2.val
    ):  # list1이 없거나 list2보다 list1이 크면 바꿔줌
        list1, list2 = list2, list1

    if list1:  # list1이 존재한다면 list1.next를 list1.next와 list2의 병합으로 지정
        list1.next = mergeTwoLists(list1.next, list2)
    return list1


"""
list1이 list2보다 작아야 함 -> list1이 크면 list2와 스왑
list1.next는 재귀를 사용해 책임 넘김
"""
