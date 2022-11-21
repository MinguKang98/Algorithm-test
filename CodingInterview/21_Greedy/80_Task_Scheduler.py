# 80_Task_Scheduler
# https://leetcode.com/problems/task-scheduler/
from typing import List
from collections import Counter


class Solution:
    # Solution 0
    def leastInterval0(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        total_count = len(tasks)
        result = []

        while total_count:
            common_task = count.most_common()

            check = 0
            for task in common_task:
                if n == 0 or (task[1] > 0 and task[0] not in result[-n:]):
                    result.append(task[0])
                    count[task[0]] -= 1
                    total_count -= 1
                    check = 1
                    break

            if check == 0:
                result.append('idle')

        return len(result)

    """
    common_task 를 순회하며 n번 간격 이내에 있다면 append
    순회가 끝나 n번 간격에 모든 글자들이 있다면 append idle
    => Time Limit Exceeded
    """

    # Solution1
    def leastInterval1(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        result = 0

        while True:
            sub_count = 0
            for task, _ in counter.most_common(n + 1):  # n+1 번씩 순회
                sub_count += 1
                result += 1
                counter.subtract(task)  # 가장 많은 task 추출
                counter += Counter()  # 0 이하 item 제거

            if not counter:
                break

            result += n - sub_count + 1  # idle 갯수 더함
            # n + 1 개가 추출이 되면 idle 이 0개, 추출 안되면 idle 1개

        return result

    """
    idle = n - sub_count + 1
    갯수가 많은 순서로 n+1 개를 추출해 sub_count, result 를 1 씩 올리고, task 를 추출한다
    sub_count 는 idle 을 셀 때 사용하는 변수로, 순회 시 몇 개의 task 르 사용햇는지 센다.
    n 번씩 추출하면 idle 이 과도하게 들어가 오답이 나오는 경우가 생긴다.
    n+1 번씩 추출하여 n+1 개가 모두 추출되면 idle 이 없이 진행되고, 모두 추출되지 않는 경우는
    n - sub_count + 1 개의 idle 이 들어간다. 
    
    Counter 의 과도한 사용으로 속도가 느림
    """

    # Solution2
    def leastInterval2(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_count = count.most_common(1)[0][1]
        idle_sum = (max_count - 1) * n

        for task, num in count.most_common()[1:]:
            idle_sum -= min(max_count - 1, num)

        return len(tasks) + max(0, idle_sum)

    """
    가장 많은 task 를 사용하여 스케줄러의 청사진을 확인할 수 있다.
    예를 들어 tasks = [A, A, A, B, B], n = 2 라면
    A__A__A 임을 알 수 있고, 그 사이에 B 와 idle 이 들어가게 된다. 
    따라서 idle 후보의 수 = (가장 많이 나온 task 수 - 1) * n 이 된다.
    이 idle 후보에 남은 task 를 집어 넣으면 최종 idle 수가 된다.
    idle 후보에 task 를 넣어 감소되는 수는 min(빼는 task 수, 가장 많이 나온 task 수 - 1) 이다
    빼는 task 가 idle 간격보다 많다면 마지막 task 의 뒤로 들어가야 하기 때문이다.
    따라서 최종 정답은 len(tasks) + idle 수 가 된다.
    
    Solution1 보다 빠름
    """


# tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
# n = 0
tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
print(Solution().leastInterval2(tasks, n))
