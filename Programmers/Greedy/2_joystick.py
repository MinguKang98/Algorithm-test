# 2_joystick
# https://school.programmers.co.kr/learn/courses/30/lessons/42860

def solution0(name):
    answer = 0
    n = len(name)
    go_back_list = [(0, 0)]  # (커서 idx, 최소값)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for idx, char in enumerate(name):
        answer += min(alphabet.index(char), 26 - alphabet.index(char))  # 위 아래
        if idx != 0:  # 좌 우
            pre_idx, pre_min = go_back_list[idx - 1][0], go_back_list[idx - 1][1]
            if char == 'A':
                go_back_list.append((pre_idx, pre_min))
            else:
                go_back_list.append((idx, pre_min + min(idx - pre_idx, pre_idx + 1)))
    return answer + go_back_list[n - 1][1]


"""
커서 좌 우 이동 시 A 는 조이스틱을 움직이지 않아도 되므로 좌 우 이동 시 차이가 나게 됨.
A : (pre_idx, pre_min)
나머지 : (idx, pre_min + min(idx - pre_idx, pre_idx + 1)
=> 오답
좌우 처리가 문제
"""


def solution0(name):
    answer = 0
    min_move = len(name) - 1
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for idx, char in enumerate(name):
        answer += min(alphabet.index(char), 26 - alphabet.index(char))  # 위 아래

        next = idx + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        # while 이후의 next 는 맨 앞에서 연속되는 A 중 마지막 A 까지의 길이. 따라서 len(name) - next 는 맨 뒤에서 연속되는
        # A 직전까지의 길이와 같다
        min_move = min(min_move, idx * 2 + len(name) - next, idx + (len(name) - next) * 2)

    answer += min_move
    return answer


"""
핵심은 연속된 A 들을 기준으로 그냥 직진 vs 직진 후 연속 A 만나면 후진 vs 후진 후 연속 A 만나면 직진 중 최소값을 찾는 것이다.
idx 는 직진 한 값, len(name) - next 는 후진한 값이므로 이를 사용해 min_move 를 갱신해준다. 
"""

# name = "JEROEN"
name = "JAN"

print(solution0(name))
