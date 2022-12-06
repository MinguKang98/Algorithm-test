# 3_cache
# https://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1
from typing import List
from collections import deque


class Solution:
    # Solution0
    def cache0(self, cacheSize: int, cities: List[str]) -> int:
        q = deque()
        exec_time = 0

        if cacheSize == 0:
            return 5 * len(cities)

        for city in cities:
            print(city, q)
            if city.upper() in q:
                exec_time += 1
            else:
                if len(q) >= cacheSize:
                    q.pop()
                q.appendleft(city.upper())
                exec_time += 5

        return exec_time

    """
    cache hit 시 순서바 바뀌는 것을 생각 못하여 해당부분 구현 X
    """

    # Solution1
    def cache1(self, cacheSize: int, cities: List[str]) -> int:
        elapsed: int = 0
        cache = deque(maxlen=cacheSize)

        for c in cities:
            c = c.lower()
            if c in cache:
                cache.remove(c)
                cache.append(c)
                elapsed += 1
            else:
                cache.append(c)
                elapsed += 5
        return elapsed

    """
    deque 의 parameter maxlen 을 사용하면 pop 을 제외할 수 있다.
    """


# cacheSize = 3
cacheSize = 2
# cacheSize = 5
# cacheSize = 0
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
# cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork","Rome"]
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

print(Solution().cache0(cacheSize, cities))
