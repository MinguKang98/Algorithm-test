# 3_dual_priority_queue
# https://school.programmers.co.kr/learn/courses/30/lessons/42628
import heapq


def solution0(operations):
    min_heap = []
    max_heap = []
    for operation in operations:
        operator, num = operation.split(' ')
        num = int(num)
        if operator == "I":
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        else:
            if len(min_heap) == 0:
                continue

            if num == 1:
                max_num = heapq.heappop(max_heap)
                min_heap.remove(-max_num)
                heapq.heapify(min_heap)
            else:
                min_num = heapq.heappop(min_heap)
                max_heap.remove(-min_num)
                heapq.heapify(max_heap)

    if len(min_heap) == 0:
        return [0, 0]
    else:
        return [-max_heap[0], min_heap[0]]


"""
최소힙인 min_heap과 최대힙인 max_heap을 사용. 하나의 힙을 heappop 하면 다른 힙은 remove 로 해당 원소
삭제 후, heapify 로 다시 heap 구조를 만든다. 
정답이긴 하지만 remove 와 heapify 의 사용으로 input 이 클 때 시간초과가 우려
"""



# operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]

operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]

print(solution0(operations))
