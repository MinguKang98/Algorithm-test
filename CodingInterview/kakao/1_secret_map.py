# 1_secret_map
# https://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1
from typing import List


class Solution:
    # Solution0 - using bitwise operation
    def secret_map0(self, n: int, arr1: List[int], arr2: List[int]) -> List[str]:
        result = []

        for i in range(n):
            k = bin(arr1[i] | arr2[i])[2:].zfill(n)
            k = k.replace('1', '#').replace('0', ' ')
            result.append(k)
        return result

    """
    풀이 방법은 정확했으나 문법 헷갈림.
    """

    # Solution1 - using bitwise operation
    def secret_map1(self, n: int, arr1: List[int], arr2: List[int]) -> List[str]:
        maps = []
        for i in range(n):
            maps.append(
                bin(arr1[i] | arr2[i])[2:]
                .zfill(n)
                .replace('1', '#')
                .replace('0', ' ')
            )
        return maps

    """
    동일한 풀이 
    """


# n = 5
# arr1 = [9, 20, 28, 18, 11]
# arr2 = [30, 1, 21, 17, 28]

n = 6
arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]

print(Solution().secret_map0(n, arr1, arr2))
