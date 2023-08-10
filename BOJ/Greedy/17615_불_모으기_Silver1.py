# 17615_불_모으기_Silver1
# https://www.acmicpc.net/problem/17615

N = int(input())
balls = input()


def solution0():
    ball_list = list(balls)
    answers = []

    cnt, red, blue = 0, 0, 0
    for ball in ball_list:  # R 오른쪽으로
        if ball == 'R':
            red += 1
        if ball == 'B' and red:
            cnt += red
            red = 0
    answers.append(cnt)

    cnt, red, blue = 0, 0, 0
    for ball in ball_list:  # B 오른쪽으로
        if ball == 'B':
            blue += 1
        if ball == 'R' and blue:
            cnt += blue
            blue = 0
    answers.append(cnt)

    ball_list.reverse()
    cnt, red, blue = 0, 0, 0
    for ball in ball_list:  # R 왼쪽으로
        if ball == 'R':
            red += 1
        if ball == 'B' and red:
            cnt += red
            red = 0
    answers.append(cnt)

    cnt, red, blue = 0, 0, 0
    for ball in ball_list:  # B 왼쪽으로
        if ball == 'B':
            blue += 1
        if ball == 'R' and blue:
            cnt += blue
            blue = 0
    answers.append(cnt)

    return min(answers)


"""
바로 옆에 다른 색있으면 모두 뛰어넘기 가능
한 가지 색만 옮길 수 있음. 한번 R 이면 R 만 옮길 수 있음

=> 아이디어는 정답 참고
색 별로 오른쪽 왼쪽으로 갈 지 탐색. 총 4 종류 수행
오른쪽으로 보내려면 오른쪽에서 왼쪽으로 탐색
왼쪽으로 보내려면 왼쪽에서 오른쪽으로 탐색
이렇게 공을 옮겨야 최소로 옮길 수 있음
=> 구현 실패. 정답 참고

red, blue 로 연속된 공 세기
만약 다른 색을 만나면 cnt 에 더해주고 red, blue 는 0으로 초기화
cnt 가 공 옮기는 수

뭉탱이 건너는 법 : 같은 색이면 누적하다가 다른 색 만나면 cnt 에 더하고 초기화
"""


def solution0():
    def move_balls(type_of_ball_to_move, s):
        s = s.lstrip(type_of_ball_to_move)
        return s.count(type_of_ball_to_move)

    return min(
        move_balls("R", balls),  # R 왼쪽으로
        move_balls("R", balls[::-1]),  # R 오른쪽으로
        move_balls("B", balls),  # B 왼쪽으로
        move_balls("B", balls[::-1]))  # B 오른쪽으로


"""
네가지 경우 중 최소값 구하는 것 같다.
lstrip 을 통해 옮기려는 색의 연속된 왼쪽 제거 후, 옮기려는 색의 갯수 세어줌
해당 값은 이동 횟수와 동일 

"""

print(solution0())
