# 16113_시그널_Silver2
# https://www.acmicpc.net/problem/16113

N = int(input())
signals = input()


def solution0():
    def is_one(idx):
        temp = 0
        if idx + 1 < K:
            for j in range(5):
                if signals[idx + 1 + j * K] == '#':
                    return False

        for j in range(5):
            if signals[idx + j * K] == '#':
                temp += 1
        return temp == 5

    num_dict = {84: '0', 79: '3', 56: '4', 86: '6', 41: '7', 91: '8', 82: '9'}
    K = len(signals) // 5
    result = ''
    i = 0
    while i < K:
        if signals[i] == '.':
            i += 1
            continue

        if is_one(i):
            result += '1'
            i += 2
        else:
            temp = 0
            for y in range(5):
                for x in range(3):
                    if signals[i + x + y * K] == '#':
                        temp += y * 3 + x
            if temp == 77:
                if signals[i + K] == '.':
                    result += '2'
                else:
                    result += '5'
            else:
                result += num_dict[temp]
            i += 4

    return result


"""
푸는 방법 맞았지만, 에러처리 모샣서 몇 번 오답
"""


def solution1():
    num_dict = {'0': ["###", "#.#", "#.#", "#.#", "###"], '2': ["###", "..#", "###", "#..", "###"],
                '3': ["###", "..#", "###", "..#", "###"],
                '4': ["#.#", "#.#", "###", "..#", "..#"], '5': ["###", "#..", "###", "..#", "###"],
                '6': ["###", "#..", "###", "#.#", "###"],
                '7': ["###", "..#", "..#", "..#", "..#"], '8': ["###", "#.#", "###", "#.#", "###"],
                '9': ["###", "#.#", "###", "..#", "###"]}

    def is_one(idx):
        for i in range(5):
            if signal_list[i][idx] != '#':
                return False
        if idx == K - 1:
            return True
        if signal_list[0][idx + 1] == '#':
            return False
        return True

    K = len(signals) // 5
    signal_list = [signals[i:i + K] for i in range(0, N, K)]
    result = ''
    i = 0
    while i < K:
        if signal_list[0][i] == '#':
            if is_one(i):
                result += '1'
                i += 1
            else:
                sig_num = []
                for j in range(5):
                    sig_num.append(signal_list[j][i: i + 3])
                for num in num_dict:
                    if num_dict[num] == sig_num:
                        result += num
                        break
                i += 3
        else:
            i += 1

    return result


"""
계산이 아닌 리스트 비교로도 해결 가능
문자열을 행렬로 변환 후, 이루어진 성분 비교로 숫자 판별
"""

print(solution1())
