# 3568_iSharp_Silver3
# https://www.acmicpc.net/problem/3568


code = input()


def solution0():
    temp_code = code[:-1]
    temp = temp_code.split(", ")
    common_type, first_var = temp[0].split(' ')

    def var_convert(var):  # 추가 변수형 앞으로
        type_start = 0
        for i in range(len(var)):
            if var[i] in '*&[]':
                type_start = i
                break

        if not type_start:
            return ' ' + var

        real_var = var[:i]
        surplus_type = var[i:]
        surplus_type = surplus_type.replace('[', '1').replace(']', '2') \
            .replace('1', ']').replace('2', '[')

        return surplus_type[::-1] + ' ' + real_var

    print(common_type + var_convert(first_var) + ';')
    for t in temp[1:]:
        print(common_type + var_convert(t) + ';')


"""
1. 쉼표로 구분된 변수들 분리
2. 공통 변수형 뽑기
3. 추가 변수형 뒤집어서 변수명 앞에 넣기
3-1. 추가 변수형 뒤집을 때 [] 가 ][ 가 되는 문제 있었음. replace 사용해 해결
"""


def solution1():
    temp_code = code.split(' ')
    common_type = temp_code[0]

    for var in temp_code[1:]:
        var = var.replace(',', '').replace(';', '')
        print(common_type, end='')

        for i in range(len(var) - 1, 0, -1):
            if not var[i].isalpha():
                if var[i] == ']':
                    print('[', end='')
                elif var[i] == '[':
                    print(']', end='')
                else:
                    print(var[i], end='')

        print(' ', end='')

        for i in range(len(var)):
            if var[i].isalpha():
                print(var[i], end='')

        print(';')


"""
문자열을 순회하며 구현한 방법
괄호들 앞으로 꺼낼 때 reverse sort 와 replace 를 쓰지 않고 뒤에서 부터 읽어서 해결
isalpha() 로 문자인지 알파벳인지 구분
"""
