# 29_Jewels_And_Stones


from typing import Counter
from collections import defaultdict

#
class Solution:
    # Solution0 - mine, using Counter
    def numJewelsInStones0(self, jewels: str, stones: str) -> int:
        result = 0
        countDict = Counter(stones)
        for jewel in jewels:
            result += 0 if countDict.get(jewel) is None else countDict.get(jewel)
        return result

    # Solution1 - using HashTable
    def numJewelsInStones1(self, jewels: str, stones: str) -> int:
        hashTable = {}
        result = 0

        for stone in stones:
            if stone not in hashTable:
                hashTable[stone] = 1
            else:
                hashTable[stone] += 1

        for jewel in jewels:
            if jewel in hashTable:
                result += hashTable[jewel]
        return result

    # Solution2 - using defaultDict
    def numJewelsInStones2(self, jewels: str, stones: str) -> int:
        hashTable = defaultdict(int)
        result = 0

        for stone in stones:
            hashTable[stone] += 1

        for jewel in jewels:
            result += hashTable[jewel]

        return result

    # Solution3 - using Counter
    def numJewelsInStones3(self, jewels: str, stones: str) -> int:
        result = 0
        countDict = Counter(stones)
        for jewel in jewels:
            result += countDict[jewel]  # Counter는 존재하지 않는 key의 값은 0을 출력
        return result

    # Solution4 - pythonic style
    def numJewelsInStones4(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)


solution = Solution()
jewels = "aA"
stones = "aAAbbbb"
print(solution.numJewelsInStones4(jewels, stones))
