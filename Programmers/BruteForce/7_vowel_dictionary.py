# 7_vowel_dictionary
# https://school.programmers.co.kr/learn/courses/30/lessons/84512

def solution0_1(word):
    weight = [781, 156, 31, 6, 1]
    num_dict = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    answer = 0
    for i in range(5 - len(word)):
        word += '#'

    for i in range(5):
        if word[i] == '#':
            break
        answer += 1 + weight[i] * num_dict[word[i]]
    return answer


"""
1. word 끝에 # 을 추가해 길이를 5로 맞춰줌
2. 규칙으로 찾은 가중치 할당
3. 계산
"""


def solution0_2(word):
    weight = [781, 156, 31, 6, 1]
    num_dict = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    answer = 0

    for i, alphabet in enumerate(word):
        answer += 1 + weight[i] * num_dict[alphabet]
    return answer


"""
불필요한 코드 제거
"""


def solution1(word):
    answer = 0
    for idx, alphabet in enumerate(word):
        answer += 1 + (5 ** (5 - idx) - 1) / (5 - 1) * "AEIOU".index(alphabet)
    return answer


"""
solution0 를 일반화 했을 때 위의 코드가 나옴
solution0 의 weight 의 차이는 a0 = 1, r = 5 인 등비수열이므로 일반항 an = (5^n - 1) / (5 - 1) 을 구할 수 있다.
"""

# word = "AAAAE"
# word = "AAAE"
# word = "I"
word = "EIO"

print(solution1(word))
