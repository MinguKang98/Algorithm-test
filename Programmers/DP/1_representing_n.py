# 1_representing_n
# https://school.programmers.co.kr/learn/courses/30/lessons/42895
from collections import defaultdict


def solution0(N, number):
    def calculate(set1, set2):
        result = set()
        for a in set1:
            for b in set2:
                result.add(a + b)
                result.add(a - b)
                result.add(a * b)
                if b:
                    result.add(a // b)
        return result

    dict = defaultdict(set)
    if N == number:
        return 1

    for i in range(1, 9):
        dict[i].add(int(str(N) * i))

    for i in range(2, 9):

        j = 1
        while j < i:
            # 계산
            temp_set = calculate(dict[j], dict[i - j])
            dict[i].update(temp_set)

            # 정답 존재 체크
            if number in dict[i]:
                return i
            j += 1

    return -1


"""
dp 사용
2회에서 8회까지 시도
무엇을 기억해야하나 : N 을 x 번 사용하여 사칙연산을 하였을 때 나오는 값
N 을 x 번 사용하여 나오는 결과 값은 반복문으로 저장된 값을 사용해 계산하여 저장
set 을 사용하여 중복인 값들은 함께 고려 => list 를 사용한 것 보다 속도 빠름

정답 조금 참고
"""

N = 5
number = 12

# N = 2
# number = 11

print(solution0(N, number))
