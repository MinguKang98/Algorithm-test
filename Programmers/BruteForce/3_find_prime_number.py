# 3_find_prime_number
# https://school.programmers.co.kr/learn/courses/30/lessons/42839
import math
from itertools import permutations


def solution0(numbers):
    def is_prime(number):
        if number == 0 or number == 1:
            return False
        for num in range(2, int(math.sqrt(number)) + 1):
            if number % num == 0:
                return False
        return True

    # 만들 수 있는 수 만들기
    answer = 0
    number_set = set([int(n) for n in numbers])
    for n in range(2, len(numbers) + 1):
        # 처음 제출한 변환
        # for idx_tuple in permutations(range(len(numbers)), n):
        #     temp = 0
        #     for i in range(n):
        #         temp = int(numbers[idx_tuple[i]]) + 10 * temp
        #     number_set.add(temp)

        # 더 나은 변환
        for temp in permutations(list(numbers), n):
            number_set.add(int("".join(temp)))

    # 소수 체크
    for number in number_set:
        if is_prime(number):
            answer += 1

    return answer


"""
만들 수 있는 모든 수를 만든 후, 소수를 체크한다.
수를 만들 대는 permutations 를 사용해 index_tuple 을 만들고, index_tuple 을 사용해 만들 수 있는 수인 temp 생성
소수체크는 어떤 수의 제곱근 보다 작거나 같은 수들을 나누었을 때 나누어 떨어지지 않는 성질을 사용했다.

처음부터 numbers 의 숫자로 permutation 해야했다. index 의 permutation 으로 계산하여 불필요한 계산이 추가되었음
"""


def solution1(numbers):
    a = set()
    for i in range(len(numbers)):
        a |= set(map(int, map("".join, permutations(list(numbers), i + 1))))

    # 0 과 1 은 소수가 아니므로 제외
    a -= set(range(0, 2))

    # 에라토스테네스의 체
    for i in range(2, int(math.sqrt(max(a))) + 1):
        a -= set(range(i * 2, max(a) + 1, i))   # i를 제외한 i의 배수들을 제거

    return len(a)


"""
알고리즘 자체는 solution0 와 동일 (모든 수 구하기 + 소수 체크) 
만들 수 있는 수를 만들 때, mpa 과 join 을 이용하여 보다 깔끔하게 생성
set 에 element 추가/삭제 시 set 의 연산들을 활용했음
소수 체크 시 에라토스테네스의 체를 사용

에라토스테네스의 체를 사용한 n 보다 작은 소수 판별 방법
1. i = 2 부터 시작해서 i 를 제외한 i 의 배수들을 모두 제거. 
2. i 가 n 의 제곱근 까지 반복
3. 남아있는 수들이 소수 
"""

# numbers = "17"
numbers = "011"

print(solution0(numbers))
