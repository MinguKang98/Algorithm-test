# 79_Queue_Reconstruction_by_Height
# https://leetcode.com/problems/queue-reconstruction-by-height/
from typing import List
import heapq


class Solution:
    def reconstructQueue1(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))

        result = []
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])
        return result

    """
    priority queue?? 그렇다면 기준은? => 기준 못찾아서 답지 봄
    => k 값 기준으로 오름차순을 생각했는데 틀린 방법
    
    heapq 에 넣어 h에 대해 내림차순 정렬
    heappop 을 통해 element 를 가져와 k번째 인덱스에 insert
    참고로, 이미 인덱스에 element 가 있으면 뒤의 element 들은 밀리게 되고, 인덱스가
    아직 없다면 맨 뒤에 insert 된다.
    """


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
print(Solution().reconstructQueue1(people))
