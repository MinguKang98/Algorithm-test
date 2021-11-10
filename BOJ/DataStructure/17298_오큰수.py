# 17298_오큰수
import sys
from typing import List

# 시간초과
def rbn() -> List[int]:
    rbn = []
    for i in range(N):
        stack = []
        for j in range(N - 1, i, -1):
            if num_list[i] < num_list[j]:
                stack.append(num_list[j])
        if len(stack) == 0:
            rbn.append(-1)
        else:
            rbn.append(stack[-1])
    return rbn


# 시간 초과
def rbn2() -> List[int]:
    rbn = []
    for i in range(N):
        stack = num_list[i + 1 :]
        stack.reverse()
        while 1:
            if len(stack) == 0:
                rbn.append(-1)
                break
            if stack[-1] <= num_list[i]:
                stack.pop(-1)
            else:
                rbn.append(stack[-1])
                break
    return rbn


"""
위의 시행들은 모두 시간복잡도가 O(n^2)이므로 시간초과 발생
stack을 사용해 O(n^2)의 시간 복잡도를  O(n)에 가깝게 조정
"""


def rbn3() -> List[int]:
    rbn = [-1] * N
    stack = []

    for i in range(N):
        # stack이 비어있지 않고 top이 비교대상보다 크면 stack 안의 element들의 위치에
        # 비교대상으로 바꿔줌
        # element만 stack에 입력시 index를 알 수 없으므로 index도 함께 입력
        while stack and stack[-1][0] < num_list[i]:
            num, idx = stack.pop()
            rbn[idx] = num_list[i]
        # 나머지의 경우는 stack에 element 추가
        stack.append([num_list[i], i])

    return rbn


# index만 stack에 넣은 경우 -> 시간이 덜 걸림
def rbn4() -> List[int]:
    rbn = [-1] * N
    stack = [0]  # 비교위해 stack에 맨 앞 index인 0 넣어줌

    for i in range(1, N):
        while stack and num_list[stack[-1]] < num_list[i]:
            rbn[stack.pop()] = num_list[i]
        stack.append(i)

    return rbn


N = int(input())
num_list = list(map(int, sys.stdin.readline().split()))
print(*rbn3())
