# 72_Sum_of_Two_Integers
# https://leetcode.com/problems/sum-of-two-integers/
class Solution:
    # Solution0
    def getSum0(self, a: int, b: int) -> int:
        # xor로 1 과 0 판단
        one = a ^ b
        # and로 올려야 되는 자리 판단
        two = (a & b) << 1
        if not two:
            return one
        else:
            # xor 과 and 에 대해 다시 수행
            # 위 수행을 and 값이 0이 될 때 까지
            return self.getSum0(one, two)

    """
    양수의 덧셈은 되지만 음수의 덧셈이 안됨
    음수는 어떻게 ?
    """

    # Solution1
    def getSum1(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF  # 32비트라 가정
        INT_MAX = 0x7FFFFFFF

        # 10진수 => 2의 보수 => 0b제거 => 32 비트 자리수 맞춰줌
        # ex) 1 => 0b1 => 1 => 00000000000000000000000000000001
        a_bin = bin(a & MASK)[2:].zfill(32)
        b_bin = bin(b & MASK)[2:].zfill(32)

        result = []
        carry = 0
        sum = 0
        for i in range(32):  # 32비트라 가정했으므로 맨 뒷자리 부터 32번 반복
            A = int(a_bin[31 - i])
            B = int(b_bin[31 - i])

            Q1 = A & B  # carry 값 생성 여부 확인
            Q2 = A ^ B  # 현재 비트 계산
            Q3 = Q2 & carry  # Q2와 carry 로 인한 올림 여부 확인
            sum = carry ^ Q2  # carry 를 더한 현재 비트 계산
            carry = Q1 | Q3  # 올릴 값 결정

            result.append(str(sum))

        if carry == 1:  # carry 값 남았다면 한번 더 올리기
            result.append('1')

        result = int(''.join(result[::-1]), 2) & MASK   # 작은 비트가 아래있으므로 reverse

        if result > INT_MAX:
            result = ~(result ^ MASK)

        return result

    # Solution2
    def getSum2(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF

        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

        if a > INT_MAX:
            a = ~ (a ^ MASK)

        return a

    """
    Solution0 와 비슷한 풀이. MASK 를 통한 자리수 조정과 음수 처리를 해준다.
    """


a = -1
b = -1
print(Solution().getSum1(a, b))
