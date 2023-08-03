# 6987_월드컵_Gold4
# https://www.acmicpc.net/problem/6987
from itertools import combinations

records = [list(map(int, input().split())) for _ in range(4)]


def solution0():
    def check(_record):
        temp = [_record[i * 3: i * 3 + 3] for i in range(6)]
        for i in range(5):
            if sum(temp[i]) != 5:
                return 0

        win_sum = sum(temp[i][0] for i in range(6))
        lose_sum = sum(temp[i][2] for i in range(6))
        if win_sum != lose_sum:
            return 0

        draw_sum = sum(temp[i][1] for i in range(6))
        if draw_sum % 2 != 0:
            return 0

        draw_cnt = sum(1 for i in range(6) if temp[i][1] != 0)
        if draw_cnt == 1:
            return 0

        return 1

    result = []
    for record in records:
        result.append(check(record))

    return ' '.join(map(str, result))


"""
가능한 결과? 승무패의 합이 5, 승의 합 == 패의 합
무승부는 판별 어떻게?? 합은 짝수 개수는 1개 이상
=> 오답 : 규칙을 만족하지 않는 경우의 수가 많음 -> 규칙이 아닌 직접 모두 탐색해야함
"""

answer = 0


def solution1():
    global answer

    result = []
    rounds = list(combinations(range(6), 2))

    def check(round_num):
        global answer

        if round_num == 15:  # 모든 라운드 계산 후 다음 라운드
            answer = 1
            for game in games:
                if sum(game) != 0:
                    answer = 0
                    break
            return

        now, target = rounds[round_num]
        for x, y in ((0, 2), (1, 1), (2, 0)):
            if games[now][x] > 0 and games[target][y] > 0:
                games[now][x] -= 1
                games[target][y] -= 1
                check(round_num + 1)
                games[now][x] += 1
                games[target][y] += 1

    for record in records:
        games = [record[i * 3: i * 3 + 3] for i in range(6)]
        answer = 0
        check(0)
        result.append(answer)
    return ' '.join(map(str, result))


"""
모든 경기를 탐색해야함 -> dfs/bfs 사용
combination 을 사용해 게임 경우의 수 생성
게임들을 순환하며 가능한 결과를 체크한 후 다음 재귀로
모든 라운드가 지난 후, games 가 모두 0이라면 가능, 0이 아닌 성분이 있으면 불가능
"""

print(solution1())
