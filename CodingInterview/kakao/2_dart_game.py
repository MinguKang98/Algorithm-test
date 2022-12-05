# 2_dart_game
# https://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1
from typing import List


class Solution:
    # Solution0
    def dart_game0(self, dartResult: str) -> int:
        dart_list = []
        for char in dartResult:
            if not dart_list:
                dart_list.append([char])
            elif char in 'SDT*#':
                dart_list[-1].append(char)
            elif char == '0' and dart_list[-1][-1] == '1':
                dart_list[-1][-1] += char
            else:
                dart_list.append([char])

        sums = [0] * 3
        for idx, sub_list in enumerate(dart_list):
            sums[idx] = int(sub_list[0])
            area = sub_list[1]

            if area == 'S':
                sums[idx] **= 1
            elif area == 'D':
                sums[idx] **= 2
            else:
                sums[idx] **= 3

            if '#' in sub_list:
                sums[idx] *= -1
            elif '*' in sub_list:
                sums[idx] *= 2
                if idx != 0:
                    sums[idx - 1] *= 2

        return sum(sums)

    """
    1. 분리 
    2. 계싼
    """

    # Solution1 - using string manipulation
    def dart_game1(self, dartResult: str) -> int:
        nums = [0]

        for s in dartResult:
            if s == 'S':
                nums[-1] **= 1
                nums.append(0)
            elif s == 'D':
                nums[-1] **= 2
                nums.append(0)
            elif s == 'T':
                nums[-1] **= 3
                nums.append(0)
            elif s == '*':
                nums[-2] *= 2
                if len(nums) > 2:
                    nums[-3] *= 2
            elif s == '#':
                nums[-2] *= -1
            else:
                nums[-1] = nums[-1] * 10 + int(s)

        return sum(nums)

    """
    풀이는 유사
    두 자리수 처리와 옵션 처리에서 큰 차이.
    Solution0 에서는 숫차 입력시 새로운 항목을 추가했으나, Solution1 은 알파벳 입력 시 새로운 항목 추가
    이 차이로 인해, Solution0 와 Solution1 은 사용하는 인덱스에서 차이가 발샘함
    초기화된 0을 사용하여 자릿수를 올려도 입력 값이 되도록 유지
    """


# dartResult = '1S2D*3T'
# dartResult = '1D2S#10S'
# dartResult = '1D2S0T'
# dartResult = '1S*2T*3S'
# dartResult = '1D#2S*3S'
# dartResult = '1T2D3D#'
dartResult = '1D2S3T*'

print(Solution().dart_game0(dartResult))
