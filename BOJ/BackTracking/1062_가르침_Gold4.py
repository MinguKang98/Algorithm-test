# 1062_가르침_Gold4
# https://www.acmicpc.net/problem/1062
from itertools import combinations

N, K = map(int, input().split())
words = []
for _ in range(N):
    # temp = input().split('anta')[1].split('tica')[0]
    # words.append(temp.lower())
    words.append(input())
alphabets = [0 for _ in range(26)]
for char in ['a', 'c', 'i', 'n', 't']:
    alphabets[ord(char) - ord('a')] = 1


def solution1():
    answer = []

    def dfs(idx, cnt, alphabets):
        if cnt == K - 5:  # 'a', 'c', 'i', 'n', 't' 를 제외하고 센 수
            temp_cnt = 0
            for word in words:
                check = True
                for w in word:
                    if not alphabets[ord(w) - ord('a')]:
                        check = False
                        break
                if check:
                    temp_cnt += 1
            answer.append(temp_cnt)
            return

        for i in range(idx, 26):
            if not alphabets[i]:
                alphabets[i] = 1
                dfs(i, cnt + 1, alphabets)
                alphabets[i] = 0

    if K < 5:
        return 0

    if K == 26:
        return N

    dfs(0, 0, alphabets)
    return max(answer)


"""
a n t i c 는 반드시 알아야 함
K가 5보다 작을 때는 anta 와 tica 를 못 읽으므로 답은 0
K가 26이면 모든 알파벳 아는 것이므로 답은 N

5<= K <26 일 경우는 어떻게??
백트래킹 고려했는데 구현 어떻게..?

1. 알파벳을 백트래킹함
2. 새로 배운 알파벳 수가 K-5 일때만 모든 단어 확인 후 셀 수 있는 단어 체크

단어 체크 로직들은 생각했는데 알파벳 백트래킹을 어떻게 해야할 지 구현 못함
"""


def solution2():
    if K < 5:
        return 0

    if K == 26:
        return N

    word_list = []
    for i in range(N):
        temp = 0
        word = words[i]
        for w in word:
            temp |= (1 << ord(w) - ord('a'))
        word_list.append(temp)

    result = 0
    alphabet_num_list = (2 ** i for i in range(26))
    for comb in combinations(alphabet_num_list, K):
        temp_word = sum(comb)

        cnt = 0
        for word in word_list:
            if temp_word & word == word:
                cnt += 1
        result = max(result, cnt)

    return result


"""
비트마스킹을 사용하는 방법

시프트 연산을 사용해 알파벳들을 숫자로 바꿈
바꾼 숫자들을 비트연산자 | 를 통해 합쳐 글자를 이루어진 알파벳들에 해당하는 숫자로 치환
ex) ac => 101

학습한 알파벳들의 비트와 글자의 비트를 & 연산 했을 때 글자의 비트가 나온다면 글자의 모든
알파벳이 학습한 알파벳에 포함된다는 뜻

solution2 는 'a, c, i, n, t' 고려 안하고 K개 의 조합 비교
"""


def solution3():
    must = {'a', 'c', 'i', 'n', 't'}
    if K < 5:
        return 0

    if K == 26:
        return N

    word_lists = []
    for word in words:
        word_lists.append(list(set(word) - must))

    bit_words = [0] * N
    for i, word in enumerate(word_lists):
        for w in word:
            bit_words[i] |= (1 << ord(w) - ord('a'))

    result = 0
    alphabet_num_list = [2 ** i for i in range(26)]
    for comb in combinations(alphabet_num_list, K - 5):
        temp_word = sum(comb)
        cnt = 0
        for bit_word in bit_words:
            if temp_word & bit_word == bit_word:
                cnt += 1
        result = max(result, cnt)

    return result


"""
solution3 는 'a, c, i, n, t' 고려해 제외하고 K-5 개 의 조합 비교
"""

print(solution2())
