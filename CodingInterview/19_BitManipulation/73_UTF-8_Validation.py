# 73_UTF-8_Validation
# https://leetcode.com/problems/utf-8-validation/
from typing import List


class Solution:
    # Solution0 -
    def validUtf8_0(self, data: List[int]) -> bool:
        cnt = 0
        for num in data:
            bin_num = bin(num)[2:].zfill(8)
            print(bin_num)
            if cnt == 0:
                if bin_num[0] == '0':
                    continue
                elif bin_num[:3] == '110':
                    cnt = 1
                elif bin_num[:4] == '1110':
                    cnt = 2
                elif bin_num[:5] == '11110':
                    cnt = 3
                else:
                    return False
            else:
                if bin_num[:2] == '10':
                    cnt -= 1
                else:
                    return False

        if cnt == 0:
            return True
        else:
            return False

    """
    cnt=0 이라면 바이트 수 체크 => 바이트 수에 다른 cnt 초기화
    0이 아니라면 바이트 수를 아는 상황이므로 처음 두 비트 10 인지 체크
    """

    # Solution1 -
    def validUtf8_1(self, data: List[int]) -> bool:
        def check(size: int):
            for i in range(start + 1, start + size + 1):
                if i >= len(data) or (data[i] >> 6) != 0b10:
                    return False
            return True

        start = 0
        while start < len(data):
            first = data[start]
            if (first >> 3) == 0b11110 and check(3):
                start += 4
            elif (first >> 4) == 0b1110 and check(2):
                start += 3
            elif (first >> 5) == 0b110 and check(1):
                start += 2
            elif (first >> 7) == 0:
                start += 1
            else:
                return False
        return True

    """
    풀이 방식 자체는 유사. >> 을 사용해 바이트의 시작 비트 체크하여 바이트 수 판단
    (바이트 수 - 1) 만큼 뒤의 바이트 들의 시작 비트 체크
    """


# data = [197, 130, 1]
# data = [235, 140, 4]
data = [248, 130, 130, 130]
print(Solution().validUtf8_0(data))
