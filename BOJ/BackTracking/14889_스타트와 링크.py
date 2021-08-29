# 14889_스타트와 링크
import sys
import itertools

# 시간 초과
def start_link(idx):
    global min_result
    if idx == N // 2:
        link_list = list(set(range(N)) - set(start_list))
        start_sum = link_sum = 0
        for i in range(idx):
            for j in range(i + 1, idx):
                start_sum += (
                    ability_list[start_list[i]][start_list[j]]
                    + ability_list[start_list[j]][start_list[i]]
                )
                link_sum += (
                    ability_list[link_list[i]][link_list[j]]
                    + ability_list[link_list[j]][link_list[i]]
                )
        diff_result = abs(start_sum - link_sum)
        min_result = min(min_result, diff_result)
    else:
        for num in range(N):
            if not check[num]:
                check[num] = True
                start_list.append(num)
                start_link(idx + 1)
                check[num] = False
                start_list.pop()


# 시간 오래 걸림
def start_link2():
    global min_result
    all_team_set = set(range(N))
    # combinations를 사용해 팀 조합을 바로 구할 수 있다
    for start_team in itertools.combinations(range(N), N // 2):
        link_team = list(all_team_set - set(start_team))

        # 각 팀 합 구함
        start_sum = link_sum = 0
        for i in range(N // 2):
            for j in range(i + 1, N // 2):
                start_sum += (
                    ability_list[start_team[i]][start_team[j]]
                    + ability_list[start_team[j]][start_team[i]]
                )
                link_sum += (
                    ability_list[link_team[i]][link_team[j]]
                    + ability_list[link_team[j]][link_team[i]]
                )
        diff_result = abs(start_sum - link_sum)
        min_result = min(min_result, diff_result)


# 합을 이용하여 계산 어려워서 구현 가능성 낮음
def start_link3():
    global min_result
    # 각 인원 당 가능한 능력치들의 합
    # i는 각 인원의 능력치 행, j는 각 인원의 능력치 열
    ability_sum_list = [
        sum(i) + sum(j) for i, j in zip(ability_list, zip(*ability_list))
    ]
    # 인원 조합이 2번 들어감, 즉 모든 능력치의 합
    all_ability_sum = sum(ability_sum_list) // 2

    diff_result = min(
        [
            abs(all_ability_sum - sum(ability))
            for ability in itertools.combinations(ability_sum_list, N // 2)
        ]
    )
    """
    전체합 12 13 14 21 23 24 31 32 34 41 42 43
    1 2뽑았다 하자
    12 13 14 21 23 24 31 32 41 42
    21  12  
    두 번 뽑힌 것들끼리 한팀 아예 안뽑힌 것들기리 한팀
    """
    min_result = min(min_result, diff_result)


if __name__ == "__main__":
    N = int(input())
    ability_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    # check = [False] * N
    # start_list = link_list = list()
    min_result = sys.maxsize
    start_link2()
    print(min_result)

"""
무엇을 BT 할 것인가?? start
언제 promising 한가?? 중복 ㄴㄴ
언제까지? 팀이 다 짜질 때까지 (idx 0부터 N//2까지)
"""
