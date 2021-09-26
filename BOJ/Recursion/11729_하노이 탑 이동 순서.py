# 11729_하노이 탑 이동 순서


def hanoi(N, start, end):
    if N == 1:
        print(start, end)
    else:
        num_list = [1, 2, 3]
        num_list.remove(start)
        num_list.remove(end)
        mid = num_list[0]
        hanoi(N - 1, start, mid)
        print(start, end)
        hanoi(N - 1, mid, end)


# 간략화 시간 & 코드 길이
def hanoi2(N, start, mid, end):
    if N == 1:
        print(start, end)
    else:
        hanoi(N - 1, start, end, mid)
        print(start, end)
        hanoi(N - 1, mid, start, end)


N = int(input())
print(2 ** N - 1)
hanoi2(N, 1, 2, 3)


"""
무엇을 재귀?? 하노이 타워의 이동을 재귀
언제 종료?? n=1일때 종료
"""
