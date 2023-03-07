# 2_biggest_number
# https://school.programmers.co.kr/learn/courses/30/lessons/42746
from functools import cmp_to_key


def solution0(numbers):
    answer = ''
    tuple_list = []
    for idx, number in enumerate(numbers):
        str_number = str(number)
        str_number += str_number[0] * (4 - len(str_number))
        tuple_list.append((str_number, idx))

    tuple_list.sort(key=lambda x: (x[0], -numbers[x[1]]), reverse=True)
    print(tuple_list)
    for _, idx in tuple_list:
        answer += str(numbers[idx])
    return str(int(answer))


"""
문자열로 정렬 후 합치기 => 오답
3 이 30 보다 앞에 오는 경우를 계산 못함. ex) 3 > 30, 7 > 776, 78 > 786
부족한 자리수는 첫 자리로 채워 전부 네 자리수로 바꾼 후, 인덱스를 가져와 문자순으로 정렬. => 오답
네 자리수로 바꿨을 때 같은 값들은 원래 더 작았던 값이 더 크다. ex) 23 > 232
바꾼수가 같을 때 길이가 더 짧은게 크게 정렬 => 오답
"""


def solution1(numbers):
    str_numbers = list(map(str, numbers))
    str_numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(str_numbers)))


"""
자리수를 맞추기 위해 첫 자리로 채우는 것이 아닌, 해당 수를 3 개 나열하여 문자열 정렬
왜 3개 나열? 숫자는 0 에서 1000 까지이므로 3자리까지 숫자를 비교하기 위해서
"""


def comparator(a, b):
    t1 = a + b
    t2 = b + a
    return (int(t1) > int(t2)) - (int(t1) < int(t2))
    # t1 이 크면 1, t2 가 크면 -1, 같으면 0. 양수면 자리를 바꾸고, 0이나 음수면 자리를 바꾸지 않는다. 


def solution2(numbers):
    str_numbers = list(map(str, numbers))
    str_numbers.sort(key=cmp_to_key(comparator), reverse=True)
    return str(int(''.join(str_numbers)))


"""
functools 의 cmp_to_key 를 이용하여 함수 선언 후, 정렬의 key 에 설정할 수 있다. 
"""

# numbers = [6, 10, 2]

# numbers = [3, 30, 34, 5, 9]

numbers = [212, 21]

print(solution1(numbers))
