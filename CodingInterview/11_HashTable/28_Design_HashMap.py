# 28_Design_HashMap

import collections


class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        idx = key % self.size
        if self.table[idx].value is None:  # ListNode 없음
            # self.table[idx] is None 으로 하면 항상 False 처리 -> defaultdict은 인덱스 조회 시 없으면 생성
            self.table[idx] = ListNode(key, value)
        else:  # ListNode 존재하면 체이닝
            temp = self.table[idx]
            while temp:
                if temp.key == key:  # key 이미 있으면 update
                    temp.value = value
                    return

                if temp.next is None:  # 초기 설정 위해
                    break
                temp = temp.next
            temp.next = ListNode(key, value)

    def get(self, key: int) -> int:
        idx = key % self.size
        if self.table[idx].value is None:  # ListNode 없음 -> no mapping
            return -1
        else:  # ListNode 존재
            temp = self.table[idx]
            while temp:
                if temp.key == key:
                    return temp.value
                temp = temp.next
            return -1  # 모든 체이닝 충 no mapping for the key

    def remove(self, key: int) -> None:
        idx = key % self.size
        if self.table[idx].value is None:  # ListNode 없음 -> no mapping
            return
        else:  # ListNode 존재
            temp = self.table[idx]
            if temp.key == key:  # 첫번째 노드일때 삭제 처리
                self.table[idx] = ListNode() if temp.next is None else temp.next
                # ListNode()가 아닌 None 할당하여 get에서 에러났었음(NoneType의 value는 없다)
                return

            prev = temp
            while temp:  # 나머지 경우 삭제 처리
                if temp.key == key:
                    prev.next = temp.next
                    return
                prev, temp = temp, temp.next


hashmap = MyHashMap()
hashmap.put(1, 1)
hashmap.put(2, 2)
print(hashmap.get(1))
print(hashmap.get(3))
hashmap.put(2, 1)
print(hashmap.get(2))
hashmap.remove(2)
print(hashmap.get(2))
