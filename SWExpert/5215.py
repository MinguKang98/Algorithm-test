# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&contestProbId=AWT-lPB6dHUDFAVT&categoryId=AWT-lPB6dHUDFAVT&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=PYTHON&select-1=4&pageSize=10&pageIndex=1

T = int(input())
for test_case in range(1, T + 1):
    N, L = map(int, input().split())  # 재료 개수, 제한 칼로리
    elements = []
    # dp[재료 인덱스][현재 칼로리] 의 값은 현재 칼로리가 가지는 최대 점수
    dp = [[0 for _ in range(L + 1)] for _ in range(N + 1)]
    for _ in range(N):
        t, k = map(int, input().split())  # 재료 점수, 칼로리
        elements.append([t, k])

    for idx in range(1, N + 1):
        for cur_calorie in range(1, L + 1):
            if elements[idx - 1][1] <= cur_calorie:
                dp[idx][cur_calorie] = max(elements[idx - 1][0] + dp[idx - 1][cur_calorie - elements[idx - 1][1]],
                                           dp[idx - 1][cur_calorie])
            else:
                dp[idx][cur_calorie] = dp[idx - 1][cur_calorie]

    print(f"#{test_case} {dp[N][L]}")

"""
칼로리에 대한 점수비 순으로 greedy 는 안될듯
dfs 백트래킹 dp 고려 => dp
조건들을 행과 열에, 구하려는 값을 dp 테이블의 값으로 넣기
특정 조건을 만족하면 테이블 갱신, 아니라면 이전 값 가져오기...
"""




