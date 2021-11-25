# 1021_회전하는 큐
import sys
from typing import List
from collections import deque

# 처음 코드
def rotateQ0(N: int, M: int, idx_list: List[int]) -> int:
    q = deque(range(1, N + 1))
    left_num, right_num = 0, 0
    while len(idx_list) != 0:
        # 뽑으려는 수가 맨 앞에 있으면
        if q[0] == idx_list[0]:  # 1번 연산 수행
            q.popleft()
            idx_list.pop(0)
        # 뽑으려는 수가 앞에 가까우면
        elif q.index(idx_list[0]) <= len(q) - q.index(idx_list[0]):  # 2번 연산 수행
            q.append(q.popleft())
            right_num += 1
        # 뽑으려는 수가 뒤에 가까우면
        else:  # 3번 연산 수행
            q.appendleft(q.pop())
            left_num += 1

    return left_num + right_num


# solution1
def rotateQ1(N: int, M: int, idx_list: List[int]) -> int:
    q = deque(range(1, N + 1))
    count = 0

    for idx in idx_list:
        while True:
            # 뽑으려는 수가 맨 앞에 있으면
            if q[0] == idx:  # 1번 연산 수행
                q.popleft()
                break
            else:
                # 뽑으려는 수가 앞에 가까우면
                # 뽑으려는 수 맨앞에 나올때 까지 2번 연산 수행
                if q.index(idx) < len(q) / 2:
                    while q[0] != idx:
                        q.append(q.popleft())
                        count += 1
                # 뽑으려는 수가 뒤에 가까우면
                # 뽑으려는 수 맨앞에 나올때 까지 3번 연산 수행
                else:
                    while q[0] != idx:
                        q.appendleft(q.pop())
                        count += 1

    return count


"""
기존 코드와 시간 비슷
"""

# solution2 - rotate 함수 사용
def rotateQ2(N: int, M: int, idx_list: List[int]) -> int:
    q = deque(range(1, N + 1))
    count = 0

    for idx in idx_list:
        while True:
            # 뽑으려는 수가 맨 앞에 있으면
            if q[0] == idx:  # 1번 연산 수행
                q.popleft()
                break
            else:
                # 뽑으려는 수가 앞에 가까우면
                # 뽑으려는 수 맨앞에 나올때 까지 2번 연산 수행
                if q.index(idx) < len(q) / 2:
                    while q[0] != idx:
                        q.rotate(-1)
                        count += 1
                # 뽑으려는 수가 뒤에 가까우면
                # 뽑으려는 수 맨앞에 나올때 까지 3번 연산 수행
                else:
                    while q[0] != idx:
                        q.rotate(1)
                        count += 1

    return count


"""
기존코드보다 시간이 더 걸림 but 편함
"""

N, M = map(int, sys.stdin.readline().split())
idx_list = list(map(int, sys.stdin.readline().split()))
print(rotateQ2(N, M, idx_list))
