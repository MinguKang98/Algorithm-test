# 71_Hamming_Distance
# https://leetcode.com/problems/hamming-distance/

class Solution:
    # Solution0 - using xor
    def hammingDistance0(self, x: int, y: int) -> int:
        xor = bin(x ^ y)
        return sum([int(i) for i in xor[2:]])

    """
    xor 연산한 결과값의 1 갯수 세기
    """

    # Solution1 - using xor
    def hammingDistance1(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')

    """
    str 에 사용하는 count 연산자 사용
    """


x = 1
y = 4
print(Solution().hammingDistance0(x, y))
