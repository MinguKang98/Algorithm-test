# 7_chuseok_traffic
# https://school.programmers.co.kr/learn/courses/30/lessons/17676
import datetime
from typing import List


class Solution:
    def chuseok_traffic0_1(self, lines: List[str]) -> int:
        # 응답 완료시간 t 와 처리시간 s 분리 + 밀리초로 변경
        timelines = []
        for line in lines:
            t, s = line.split("2016-09-15 ")[-1].split(' ')
            hh, mm, ss = t.split(':')
            end_time = int(hh) * 60 * 60 * 1000 + int(mm) * 60 * 1000 + int(float(ss) * 1000)
            start_time = end_time - int(float(s[:-1]) * 1000) + 1
            timelines.append([start_time, end_time])

        # 1초 짜리 윈도우를 돌며 갯수 갱신
        result = 0
        search_times = []
        for search_time in search_times:
            count = 0
            for start, end in timelines:
                if start <= search_time <= end or start <= search_time + 999 <= end:
                    count += 1
            result = max(result, count)
        return result

    """
    1 밀리초마다 탐색? 부하 상당함 => 어떤 패턴으로 슬라이스 윈도우?? => 끝나는 시간 ~ 끝나는 시간 + 999 의 범위에
    몇 개 있는지 세기
    부분 성공
    """

    def chuseok_traffic0_2(self, lines: List[str]) -> int:
        # 응답 완료시간 t 와 처리시간 s 분리 + 밀리초로 변경
        timelines = []
        search_times = []
        for line in lines:
            t, s = line.split("2016-09-15 ")[-1].split(' ')
            hh, mm, ss = t.split(':')
            end_time = int(hh) * 60 * 60 * 1000 + int(mm) * 60 * 1000 + int(float(ss) * 1000)
            start_time = end_time - int(float(s[:-1]) * 1000) + 1
            timelines.append([start_time, end_time])
            search_times.append(start_time)
            search_times.append(end_time)

        search_times.sort()
        # 1초 짜리 윈도우를 돌며 갯수 갱신
        result = 0
        for search_time in search_times:
            count = 0
            for start, end in timelines:
                if start <= search_time <= end or start <= search_time + 999 <= end:
                    count += 1
            result = max(result, count)
        return result

    """
    시작시간 구간 + 끝나는 시간 구간 탐색
    그래도 오답
    """

    def chuseok_traffic0_3(self, lines: List[str]) -> int:
        # 응답 완료시간 t 와 처리시간 s 분리 + 밀리초로 변경
        timelines = []
        search_times = []
        for line in lines:
            t, s = line.split("2016-09-15 ")[-1].split(' ')
            hh, mm, ss = t.split(':')
            end_time = int(hh) * 60 * 60 * 1000 + int(mm) * 60 * 1000 + int(float(ss) * 1000)
            start_time = end_time - int(float(s[:-1]) * 1000) + 1
            timelines.append([start_time, end_time])
            search_times.append(start_time)
            search_times.append(end_time)

        search_times.sort()
        # 1초 짜리 윈도우를 돌며 갯수 갱신
        result = 0
        for search_time in search_times:
            count = 0
            for start, end in timelines:
                if start <= search_time <= end or \
                        start <= search_time + 999 <= end or \
                        (search_time < start and end < search_time + 999):
                    count += 1
            result = max(result, count)
        return result

    """
    이전 풀이들은 윈도우 안에 로그가 들어가는 경우가 제외되어 오답이 나옴
    해당 경우를 추가하니 정답처리
    """

    def chuseok_traffic1(self, lines: List[str]) -> int:
        # 응답 완료시간 t 와 처리시간 s 분리 + 밀리초로 변경
        combined_logs = []
        for line in lines:
            t, s = line.split("2016-09-15 ")[-1].split(' ')
            hh, mm, ss = t.split(':')
            end_time = int(hh) * 60 * 60 * 1000 + int(mm) * 60 * 1000 + int(float(ss) * 1000)
            start_time = end_time - int(float(s[:-1]) * 1000) + 1
            combined_logs.append((start_time, 1))
            combined_logs.append((end_time, -1))

        accumulated = 0
        max_requests = 1
        combined_logs.sort(key=lambda x: x[0])
        for i, elem1 in enumerate(combined_logs):
            current = accumulated

            # 1초 짜리 윈도우를 돌며 갯수 갱신
            for elem2 in combined_logs[i:]:
                if elem2[0] - elem1[0] > 999:  # 범위 안에 없으면 break
                    break
                if elem2[1] > 0:  # 시작 요청만 더한다. 범위 내의 종료 요청은 accumulated 에 포함되어 있다
                    current += elem2[1]
            max_requests = max(max_requests, current)
            accumulated += elem1[1]  # 시작 시 1, 종료 시 -1 을 더해 누적된 요청 수를 계산한다.
        return max_requests

    """
    전처리는 동일하게 + 윈도우 처리부분은 답지 참고
    구간 내 요청 수에 변화가 생기는 시점은 요청의 시작과 종료의 경우이므로 그 때만 윈도우를 계산한다.
    """

    def chuseok_traffic2(self, lines: List[str]) -> int:
        combined_logs = []
        for log in lines:
            logs = log.split(' ')
            timestamp = datetime.datetime.strptime(logs[0] + ' ' + logs[1],
                                                   "%Y-%m-%d %H:%M:%S.%f").timestamp()
            combined_logs.append((timestamp, -1))
            combined_logs.append((timestamp - float(logs[2][:-1]) + 0.001, 1))

        accumulated = 0
        max_requests = 1
        combined_logs.sort(key=lambda x: x[0])
        for i, elem1 in enumerate(combined_logs):
            current = accumulated

            for elem2 in combined_logs[i:]:
                if elem2[0] - elem1[0] > 0.999:  # 범위 안에 없으면 break
                    break
                if elem2[1] > 0:  # 시작 요청만 더한다. 범위 내의 종료 요청은 accumulated 에 포함되어 있다
                    current += elem2[1]
            max_requests = max(max_requests, current)
            accumulated += elem1[1]  # 시작 시 1, 종료 시 -1 을 더해 누적된 요청 수를 계산한다.

        return max_requests

    """
    라이브러리를 사용한 전처리 + 윈도우 처리
    """

# lines = [
#     "2016-09-15 01:00:04.001 2.0s",
#     "2016-09-15 01:00:07.000 2s"
# ]

# lines = [
#     "2016-09-15 01:00:04.002 2.0s",
#     "2016-09-15 01:00:07.000 2s"
# ]

lines = [
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
]

print(Solution().chuseok_traffic2(lines))
