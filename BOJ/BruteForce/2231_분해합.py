# 2231_분해합

# 느림
def div_sum(raw_N):
    N = int(raw_N)
    arr = []
    # 무엇을 탐색?? 분해합 후보들(N부터 1까지)
    for i in range(N, 0, -1):
        ans = i
        raw_ans = str(i)
        ans += sum(list(map(int, list(raw_ans))))
        if ans == N:
            arr.append(i)

    if len(arr) == 0:
        print(0)
    else:
        print(min(arr))


# 빠름
def div_sum2(N):
    # 분해수는 항상 N-9*6보다 큼
    for i in range(max(1, N - 54), N):
        if sum(map(int, str(i))) + i == N:
            print(i)  # 작은 수부터 탐색했으므로 처음 나오면 최솟값
            exit(0)
    print(0)


if __name__ == "__main__":
    N = int(input())
    div_sum2(N)
