# 22_Daily_Temperature
from typing import List
from unittest import result

from black import diff


class Solution:
    # Solution0 - mine/ 2중 loop
    def dailyTemperatures0(self, temperatures: List[int]) -> List[int]:
        result = []
        N = len(temperatures)
        for num1 in range(N - 1):
            diff = 1
            for num2 in range(num1 + 1, N):
                if temperatures[num2] > temperatures[num1]:
                    result.append(diff)
                    break
                else:
                    diff += 1
                    if num2 == N - 1:
                        result.append(0)
        result.append(0)
        return result

    """
    Time Limit Exceed
    """

    # Solution1 - Stack
    def dailyTemperatures1(self, temperatures: List[int]) -> List[int]:
        result, stack = [0] * len(temperatures), []

        for idx, temp in enumerate(temperatures):
            while (
                stack and temp > temperatures[stack[-1]]
            ):  # 현제 temp이 stack top의 temp보다 크다면(=온도 올라갈때) result에 값 입력
                # 고점에서 stack에 모인 idx들 값 설정해줌
                top = stack.pop()
                result[top] = idx - top
            stack.append(idx)  # 항상 stack에 idx 추가

        return result
