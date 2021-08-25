# 9663_N-Queen

# 답은 맞음 but 시간초과
def promising(depth, col):
    # num이 배치된 queen 들과 만나면 안됨
    if depth == 0:
        return True
    for row in range(1, depth + 1):
        # 같은 열 ㄴㄴ 대각선 위 ㄴㄴ
        if arr[row] == col or depth + 1 - row == abs(arr[row] - col):
            return False
    return True


def n_queen(depth):
    global result
    if depth == N:
        result += 1
        return
    else:
        for col in range(1, N + 1):
            if promising(depth, col):
                arr.append(col)
                n_queen(depth + 1)
                arr.pop()


# PyPy3 수행 시 통과
def promising2(depth):
    # depth열에 배치된 queen이 다른 queen들과 만나면 안됨
    for row in range(depth):
        # 같은 열 ㄴㄴ  or 같은 대각선 ㄴㄴ
        if arr[row] == arr[depth] or depth - row == abs(arr[row] - arr[depth]):
            return False
    return True


def n_queen2(depth):
    global result
    if depth == N:
        result += 1
    else:
        for col in range(N):  # 0열 ~N-1열까지
            arr[depth] = col  # depth행의 queen이 col에 있다하자
            if promising2(depth):  # promising 판단
                n_queen2(depth + 1)


# 행과 대각선을 나타내는 행렬 사용
def n_queen3(i):
    global result
    if i == N:
        result += 1
        return
    else:
        for j in range(N):  # 0열 ~N-1열까지
            if not (
                row[j] or right_for_diag[i + j] or right_rev_diag[i - j + N - 1]
            ):  # 모두 False여야 promising, 즉 해당 열과 두 대각선이 안 쓰여짐
                row[j] = right_for_diag[i + j] = right_rev_diag[
                    i - j + N - 1
                ] = True  # i행 j열 기준 해당 열과 두 대각선은 쓰여졌다고 표시
                n_queen3(i + 1)
                row[j] = right_for_diag[i + j] = right_rev_diag[
                    i - j + N - 1
                ] = False  # 반환


if __name__ == "__main__":
    N = int(input())
    # arr = [0] * N
    row, right_for_diag, right_rev_diag = (
        [False] * N,
        [False] * (2 * N - 1),
        [False] * (2 * N - 1),
    )

    result = 0
    n_queen3(0)
    print(result)

"""

"""
