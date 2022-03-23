# 27_Merge_k_Sorted_Lists
import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Solution0 - my solution
    def mergeKLists0(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result_list = []
        result = result_ListNode = ListNode(None)
        # list로 변환
        for list in lists:
            while list is not None:
                result_list.append(list.val)
                list = list.next

        # 정렬
        result_list.sort()

        # ListNode로 변환
        for num in result_list:
            result_ListNode.next = ListNode(num)
            result_ListNode = result_ListNode.next

        return result.next

    # Solution1 - using PriorityQueue(heapq)
    def mergeKLists1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = result = ListNode(None)
        heap = []

        # 연결리스트 루트를 힙에 저장
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
                # heapq.heappush(heap, (lists[i].val, lists[i]))로 저장 가능하지만 heapq는 중복 지원 안해 error
                # -> error 방지 위해 i 추가

        # 힙 추출 이후 다음 노드 다시 저장
        while heap:
            # pop 하면 가장 작은 값 나옴 -> 그 노드 다음 값 heaq에 다시 넣어라
            node_tuple = heapq.heappop(heap)
            idx = node_tuple[1]

            result.next = node_tuple[2]
            result = result.next

            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next
