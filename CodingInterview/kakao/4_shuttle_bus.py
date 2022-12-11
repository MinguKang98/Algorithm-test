# 4_shuttle_bus
# https://school.programmers.co.kr/learn/courses/30/lessons/17678
from typing import List


class Solution:
    # Solution0
    def shuttle_bus0(self, n: int, t: int, m: int, timetable: List[str]) -> str:
        bus_table = []
        for i in range(n):
            hour = str(9 + (i * t) // 60).zfill(2)
            minute = str(0 + (i * t) % 60).zfill(2)
            bus_table.append(f"{hour}:{minute}")

        timetable.sort()
        bus_index = 0
        cnt = 0
        empty = False
        for time in timetable:
            if time == '23:59':
                empty = True
                continue
            elif time <= bus_table[bus_index]:
                cnt += 1
            else:
                bus_index += 1
                cnt = 1

            if cnt == m:
                bus_index += 1
                cnt = 0

        if cnt != 0:
            return bus_table[bus_index]
        else:
            if empty:
                return bus_table[-1]

            last = timetable[-1]
            hour, minute = last.split(':')
            if minute == '00':
                return f"{str(int(hour) - 1).zfill(2)}:59"
            else:
                return f"{hour}:{str(int(minute) - 1).zfill(2)}"

    """
    버스 가장 늦게 타는 법
    
    timetable 은 다른 작업 없이 대소비교, 정렬 가능
    
    n, t 사용하여 bus 시간 계산
    n, m 사용해서 총 탈 수 있는 인원 계산
    
    버스에 자리가 남는다면 버스 출발시간
    다 찼다면 마지막 인원 탑승시간 - 1
    => 오답(실패 + 런타임 에러)
    """

    # Solution1
    def shuttle_bus1(self, n: int, t: int, m: int, timetable: List[str]) -> str:
        timetable = [int(time[:2]) * 60 + int(time[3:]) for time in timetable]
        timetable.sort()

        current = 540
        for _ in range(n):
            for _ in range(m):
                if timetable and timetable[0] <= current:
                    candidate = timetable.pop(0) - 1
                else:
                    candidate = current
            current += t

        hour, minute = divmod(candidate, 60)
        return str(hour).zfill(2) + ':' + str(minute).zfill(2)

    """
    current 는 버스 시간, candidate 는 콘의 버스 탑승 시간의 후보
    대기가 있는 경우 1분 전 탑승 & 대기가 없는 경우 버스 버스 시간에 탑승
    timetalbe 이 있고 timetable[0] <= current 라면 먼저 온 사람보다 빨리 타야하므로
    candidate = timetable.pop(0) - 1 으로 설정. 이때 pop 을 통해 해당 시간에 탑승한 인원은
    다음 루프에 고려하지 않음, 즉 탑승 시킴
    timetable 이 없거나 timetable[0] > current 라면 candidate = current 로 설정하여 해당 인원은
    다음 루프에서도 고려하도록 함, 즉 다음 버스 때 탑승 고려
        
    전체적인 알고리즘은 유사하나 구현이 잘못된 듯 하다
    """


# n = 1
# t = 1
# m = 5
# timetable = ["08:00", "08:01", "08:02", "08:03"]

# n = 2
# t = 1
# m = 2
# timetable = ["09:00", "09:00", "09:00", "09:00"]

# n = 2
# t = 10
# m = 2
# timetable = ["09:10", "09:09", "08:00"]

# n = 1
# t = 1
# m = 5
# timetable = ["00:01", "00:01", "00:01", "00:01", "00:01"]

# n = 1
# t = 1
# m = 1
# timetable = ["23:59"]

n = 10
t = 60
m = 45
timetable = ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
             "23:59", "23:59", "23:59", "23:59"]

print(Solution().shuttle_bus0(n, t, m, timetable))
