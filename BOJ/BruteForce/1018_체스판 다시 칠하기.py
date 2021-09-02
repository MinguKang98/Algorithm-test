# 1018_체스판 다시 칠하기
import sys


def chess_coloring():
    result = 64
    for k in range(2):
        for i in range(N - 7):  # 체스판 행
            for j in range(M - 7):  # 체스판 열
                cnt = 0
                # 검사
                for x in range(8):  # 8x8 행
                    for y in range(8):  # 8x8 열
                        if (
                            chess[i + x][j + y] != ans[abs((i + x) % 2 - k)][y]
                        ):  # 비교했는데 다르다면 count
                            cnt += 1
                result = min(result, cnt)
    print(result)


# for문이 하나 줄고 계산 줄어 시간 더 짧음
def chess_coloring2():
    result = 64
    for i in range(N - 7):  # 체스판 행
        for j in range(M - 7):  # 체스판 열
            cnt_white = 0  # 처음 흰색 시작 체스판 기준
            cnt_black = 0  # 처음 검은색 시작 체스판 기준
            # 검사
            for x in range(i, i + 8):  # 8x8 행
                for y in range(j, j + 8):  # 8x8 열
                    if (x + y) % 2 == 0:  # 홀수 대각선
                        if chess[x][y] != "W":
                            cnt_white += 1
                        if chess[x][y] != "B":
                            cnt_black += 1
                    else:  # 짝수 대각선
                        if chess[x][y] != "W":
                            cnt_black += 1
                        if chess[x][y] != "B":
                            cnt_white += 1
            result = min(result, cnt_white, cnt_black)
    print(result)


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    # ans = ["WBWBWBWB", "BWBWBWBW"]
    chess = [input() for _ in range(N)]
    chess_coloring2()


"""
무엇을 완전탐색 할 것인가?? chess(체스판)
어떤 조건에 ?? 8X8 이 다시 칠해야 하는 개수 확인                                                                                                                                                   
"""
