# 74_Number_of_1_Bits
# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    # Solution0 - using count
    def hammingWeight0(self, n: int) -> int:
        num = bin(n)[2:].zfill(32)
        return num.count('1')

    # Solution1 - using count
    def hammingWeight1(self, n: int) -> int:
        # return bin(n ^ 0b00000000000000000000000000000000).count('1') XOR 을 통해 1 체크
        # return bin(n ^ 0).count('1')  => 파이썬이 자동 처리
        return bin(n).count('1')  # XOR 0 이므로 생략 가능하다

    # Solution2 - using bit maninpulation
    def hammingWeight2(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count

    """
    1을 뺀 값과 AND 연산을 하면 비트가 1 씩 빠진다 (수가 1 작아지는 건 아님)
    """


n = 0b00000000000000000000000000001011
print(Solution().hammingWeight0(n))
