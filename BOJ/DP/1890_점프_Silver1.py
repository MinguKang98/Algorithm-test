# 1890_점프_Silver1
# https://www.acmicpc.net/problem/1890

N = int(input())
boards = [list(map(int, input().split())) for _ in range(N)]


def solution0():
    dp = [[0 for _ in range(N)] for _ in range(N)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(N):
            if i == N - 1 and j == N - 1:
                break

            if 0 <= j + boards[i][j] < N:
                dp[i][j + boards[i][j]] += dp[i][j]
            if 0 <= i + boards[i][j] < N:
                dp[i + boards[i][j]][j] += dp[i][j]

    return dp[-1][-1]


"""
bfs 로 하려다가 바꿈 => 특정 위치를 계속 다닐 수 있어서 visted 를 체크하면 안됨
=> 현재 위치까지 오는 경로의 수를 저장할 필요가 있음 => dp로 풀어야함
queue 를 사용해서 풀려다가 dp의 값이 모두 0 이고 dp[0][0] 만 1이라면 
그냥 이중루프 쓰면 됨
"""

print(solution0())
