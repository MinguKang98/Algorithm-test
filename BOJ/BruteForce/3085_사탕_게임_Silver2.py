# 3085_사탕_게임_Silver2
# https://www.acmicpc.net/problem/3085

N = int(input())
boards = []
for _ in range(N):
    boards.append(list(input()))


def check_max_candy(temp_boards):  # 보드에서 같은 색으로 이루어진 가장 긴 부분 찾기
    temp_max = 1
    for i in range(N):
        temp_cnt = 1
        for j in range(N - 1):  # 행에서 가장 긴 부분 찾기
            if temp_boards[i][j] == temp_boards[i][j + 1]:
                temp_cnt += 1
                temp_max = max(temp_max, temp_cnt)
            else:
                temp_cnt = 1

        temp_cnt = 1
        for j in range(N - 1):  # 열에서 가장 긴 부분 찾기
            if temp_boards[j][i] == temp_boards[j + 1][i]:
                temp_cnt += 1
                temp_max = max(temp_max, temp_cnt)
            else:
                temp_cnt = 1

    return temp_max


answer = 1
for i in range(N):
    for j in range(N):
        if j + 1 < N and boards[i][j] != boards[i][j + 1]:
            boards[i][j], boards[i][j + 1] = boards[i][j + 1], boards[i][j]
            answer = max(answer, check_max_candy(boards))
            boards[i][j], boards[i][j + 1] = boards[i][j + 1], boards[i][j]

        if i + 1 < N and boards[i][j] != boards[i + 1][j]:
            boards[i][j], boards[i + 1][j] = boards[i + 1][j], boards[i][j]
            answer = max(answer, check_max_candy(boards))
            boards[i][j], boards[i + 1][j] = boards[i + 1][j], boards[i][j]

print(answer)

"""
1. 색 다른 두칸 교환
2. 전체에세 가장 긴 연속부분 계산
3. 반복
아이디어는 있었지만 너무 오래걸릴 거 같아 시도 안하고 풀이 참조 => 이게 맞았음
완전탐색은 겁먹지 말고 도전부터

상하좌우 다 교환하지 말고 현재 위치 기준 오른쪽과 아래만 교환

"""
