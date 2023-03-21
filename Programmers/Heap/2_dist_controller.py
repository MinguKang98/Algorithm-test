# 2_dist_controller
# https://school.programmers.co.kr/learn/courses/30/lessons/42627
import heapq


def solution0(jobs):
    n = len(jobs)
    answer = 0
    jobs.sort()
    heapq.heapify(jobs)
    node = heapq.heappop(jobs)
    end = node[0] + node[1]
    answer += node[1]
    answer_list = [node[1]]

    while jobs:
        node = heapq.heappop(jobs)
        if node[0] < end:
            temp_jobs = [node]
            while jobs and jobs[0][0] < end:
                temp_jobs.append(heapq.heappop(jobs))

            # 소요 시간 게산
            min_idx = 0
            min_take = 1000
            for idx, temp_job in enumerate(temp_jobs):
                if (end - temp_job[0]) + temp_job[1] < min_take:
                    min_idx = idx

            # 소요시간 작은거 선택후 계산

            start, take = temp_jobs[min_idx]
            answer += (end - start) + take
            end += take

            # 나머지는 push
            for i in range(len(temp_jobs)):
                if i != min_idx:
                    heapq.heappush(jobs, temp_jobs[i])
        else:
            answer += node[1]
            end = node[0] + node[1]
            answer_list.append(node[1])

    return answer // n


"""
평균 시간이 가장 짧으려면 어떤 순서로 계산해야하나 => 소요시간의 합이 가장 작아야함 => 
end 는 job 마다 job[1]을 더함
소요시간(요청 ~ 종료시간)은 안 겹치면 (end < job[0]) job[1], 겹치면 (end > job[0]) (end-job[0]) + job[1] 

jobs 를 요청 시간으로 정렬된 우선순위 큐에 보관
가장 작은거 꺼내서 job[1] 전에 시작하는 애들 다 pop 하고 계산하여 소요시간 작은거 선택 후 안쓰는건 다시 push 
=> 오답 20 문제 중 1~13, 16 실패
"""


def solution1(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    heap = []

    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])

        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += (now - current[1])
            i += 1
        else:
            now += 1

    return answer // len(jobs)


"""
i 는 처리된 job 의 갯수, now 는 현재 시간을 의미한다.
우선, 현재 시점에서 처리할 수 있는 작업, 즉 시작 시간이 start 초과 now 이하인 job 들을 heap 에 저장한다.
heap 은 소요시간 기준으로 정렬된다.

처리할 수 있는 작업이 있다면 start 는 now 로 바꾸고, now 는 current 의 처리 시간만큼 증가시킨다.
그리고 answer 에는 요청에서 종료까지의 시간인 (기존 now - current[1]) + current[0] 을 더해준다. 
이때,  이전에 now 에 current[0] 를 더했으므로 (기존 now - current[1]) + current[0] = now - current[1] 이다.
처리할 수 있는 작업이 없다면 현재 시간을 1 늘린다.

job 들을 heap 에 넣는 것은 좋은 접근이었지만, 처리 가능한 job 들만 heap 에 넣어 처리했어야 했음
처리할 수 있는 작업들 중 소요시간이 가장 짧은 것을 골라야 평균이 짧아진다. 이 부분을 놓쳤다.
공백 시간을 처리하기 위해 solution0 같이 복잡한 처리를 하지 않으려면, 현재 시간도 같이 체크했어야함
"""

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution0(jobs))
