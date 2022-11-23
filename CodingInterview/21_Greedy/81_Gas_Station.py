# 81_Gas_Station
# https://leetcode.com/problems/gas-station/
from typing import List


class Solution:
    def canCompleteCircuit0(self, gas: List[int], cost: List[int]) -> int:
        fuel = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(fuel) < 0:
            return -1

        n = len(fuel)
        for i in range(n):
            total = 0
            for j in range(n):
                total += fuel[(i + j) % n]
                if total < 0:
                    break
            if total >= 0:
                return i
        return -1

    """
    fuel 의 총합이 0 미만이면 출발점이 존재하지 않는다.
    시작점 부터 시작 시 fuel 의 합이 항상 0 이상 이여야 한다. => 어떻게 구현?? bruteforce
    => O(n^2) Time Limit Exceeded
    """

    # Solution1
    def canCompleteCircuit1(self, gas: List[int], cost: List[int]) -> int:
        for start in range(len(gas)):
            fuel = 0
            for i in range(start, len(gas) + start):
                index = i % len(gas)

                can_travel = True
                if gas[index] + fuel < cost[index]:
                    can_travel = False
                    break
                else:
                    fuel += gas[index] - cost[index]

            if can_travel:
                return start
        return -1

    """
    Solution0 처럼 출발점을 기준으로 모든 주유소를 방문하는 방법이다.
    => O(n^2) Time Limit Exceeded
    """

    # Solution2
    def canCompleteCircuit2(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start, fuel = 0, 0
        for i in range(len(gas)):
            if gas[i] + fuel < cost[i]:  # 성립하지 않는 경우
                start = i + 1  # 출발점 밀어내고 fuel 초기화
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
        return start

    """
    sum(gas) < sum(cost) 일 때 -1 을 return 하면 출발점이 있는 경우만 남는다.
    남은 case 에 대해서 전체 주유소를 방문하며 성립되지 않는 경우는 출발점을 뒤로 밀어내는 방법을
    사용한다.
    O(n) 의 시간복잡도를 가지게 된다
    
    Solution0 에서 fuel 의 총합이 0 보다 크면 전체 방문가능한 출발점이 항상 존재하지는 않는다고
    생각했지만 항상 존재한다.
    """


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(Solution().canCompleteCircuit0_2(gas, cost))
