# 84_Different_Ways_to_Add_Parentheses
# https://leetcode.com/problems/different-ways-to-add-parentheses/
from typing import List


class Solution:
    # Solution0 - using divide&conquer
    def diffWaysToCompute0(self, expression: str) -> List[int]:
        result = []
        if expression.isdigit():
            result.append(int(expression))
        else:
            for i in range(len(expression)):
                if expression[i] == '+' or expression[i] == '-' or expression[i] == '*':
                    list1 = self.diffWaysToCompute0(expression[:i])
                    list2 = self.diffWaysToCompute0(expression[i + 1:])
                    for num1 in list1:
                        for num2 in list2:
                            if expression[i] == '+':
                                ans = num1 + num2
                            elif expression[i] == '-':
                                ans = num1 - num2
                            else:
                                ans = num1 * num2
                            result.append(ans)
        return result

    """
    어떻게 divide ? 연산자 기준으로 나눔 
    어떻게 conquer? 연산을 한 값을 return 한다고 생각하여 연산자 기준으로 나눈 두 식의
    값을 받아와 연산자로 계산 
    이때 받아오는 값은 가능한 결과값의 list 이므로 두 list 를 모두 돌며 계산해야함
    """

    # Solution1 - using divide&conquer
    def diffWaysToCompute1(self, expression: str) -> List[int]:
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))
            return results

        if expression.isdigit():
            return [int(expression)]

        results = []
        for index, value in enumerate(expression):
            if value in "-+*":
                left = self.diffWaysToCompute1(expression[:index])
                right = self.diffWaysToCompute1(expression[index + 1:])

                results.extend(compute(left, right, value))
        return results

    """
    전체적인 풀이 방법은 Solution0 와 같다.
    Solution0 는 element 의 계산 값을 result 에 바로 넣으므로 append 를 쓰는 반면
    Solution1 은 compute 를 사용해 계산한 값의 list 를 받아오므로 extend 를 사용
    eval 을 사용해 if-elif-else 문 축약
    """


expression = "2-1-1"
# expression = "2*3-4*5"
print(Solution().diffWaysToCompute0(expression))
