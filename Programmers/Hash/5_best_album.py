# 5_best_album
# https://school.programmers.co.kr/learn/courses/30/lessons/42579
from collections import defaultdict


def solution0(genres, plays):
    answer = []
    custom_dict = defaultdict(list)
    temp_cnt_dict = defaultdict(int)
    cnt_dict = dict()
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        custom_dict[genre].append((play, idx))
        temp_cnt_dict[genre] += play

    for key, value in temp_cnt_dict.items():
        cnt_dict[value] = key

    for key in custom_dict.keys():
        custom_dict[key].sort(key=lambda x: (-x[0], x[1]))

    for total in sorted(list(cnt_dict.keys()), reverse=True):
        temp_list = custom_dict[cnt_dict[total]]
        if len(temp_list) == 1:
            answer.append(temp_list[0][1])
        else:
            answer.append(temp_list[0][1])
            answer.append(temp_list[1][1])

    return answer


"""
custom_dict : genre 를 key 로, (play, idx) 를 value 로 가지는 dictionary
temp_cnt_dict : genre 의 plays 수 의 총합을 구하기 위한 dictionary. genre 가 key, plays 의 합이 value
cnt_dict : temp_cnt_dict 의 key 와 value 가 바뀐 dictionary. 
내림차순으로 정렬된 cnt_dict.keys() 를 순회하며 cnt_dict[key] 를 조회하면 1번 기준 만족
temp_list = cusotm_dict[cnt_dict[key]] 는 위에서 2, 3 번 조건을 만족하게 정렬되어 있으므로
temp_list[0][0] 또는 temp_list[0][1] 만 추가하면 됨
"""


def solution1(genres, plays):
    answer = []
    d = {e: [] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1], e[2]])
    genre_sort = sorted(list(d.keys()), key=lambda x: sum(t[0] for t in d[x]), reverse=True)
    for g in genre_sort:
        temp = [e[1] for e in sorted(d[g], key=lambda x: (-x[0], x[1]))]
        answer += temp[:min(len(temp), 2)]
    return answer


"""
solution0 에서는 temp_ctn_dict 을 구하고 k, v 값을 바꿔 cnt_dict 을 구했지만 solution1 에서는 genre 의 plays 수의
총합을 기준으로 d.keys() 를 정렬한 리스트를 사용함
또한 길이가 1인 list 판열 시 if-else 를 사용했는데, solution1 에서는 min 으로 해결 
"""

# genres = ["classic", "pop", "classic", "classic", "pop"]
# plays = [500, 600, 150, 800, 2500]
genres = ["classic", "pop", "classic", "classic", "pop", "classic"]
plays = [500, 600, 150, 800, 2500, 500]
print(solution0(genres, plays))
