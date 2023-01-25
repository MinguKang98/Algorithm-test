# 2_mock_exam
# https://school.programmers.co.kr/learn/courses/30/lessons/42840
from collections import defaultdict


def solution0(answers):
    supo1 = [1, 2, 3, 4, 5] * 2000
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    cnt1, cnt2, cnt3 = 0, 0, 0
    for i in range(len(answers)):
        cnt1 += (supo1[i] == answers[i])
        cnt2 += (supo2[i] == answers[i])
        cnt3 += (supo3[i] == answers[i])

    custom_dict = defaultdict(list)
    custom_dict[cnt1].append(1)
    custom_dict[cnt2].append(2)
    custom_dict[cnt3].append(3)

    return custom_dict[max(custom_dict.keys())]


"""
시험은 최대 10,000 문제이므로 수포자들의 정답지를 모두 세팅하여 시작
정답 갯수인 cnt1, cnt2, cnt3 를 구한 후, key 가 cnt 이고 value 가 수포자 번호인 defaultdict 을 생성하여 가장 많이
정답을 맞춘 사람의 리스트를 구함
"""


def solution1(answers):
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == supo1[idx % len(supo1)]:
            score[0] += 1
        if answer == supo2[idx % len(supo2)]:
            score[1] += 1
        if answer == supo3[idx % len(supo3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx + 1)

    return result


"""
정답지를 미리 세팅하지 않고 나머지를 사용하여 정답 조회, cnt1, cnt2, cnt3 로 선언하는 것이 아닌 list 로 묶어서 선언
"""

# answers = [1, 2, 3, 4, 5]
answers = [1, 3, 2, 4, 2]

print(solution0(answers))
