# 1495_기타리스트_Silver1
# https://solved.ac/search?query=1495

N, S, M = map(int, input().split())
volumes = list(map(int, input().split()))


def solution0():
    dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    dp[0][S] = 1

    for i in range(N):
        for j in range(M + 1):
            if dp[i][j] == 1:
                if 0 <= j + volumes[i] <= M:
                    dp[i + 1][j + volumes[i]] = 1
                if 0 <= j - volumes[i] <= M:
                    dp[i + 1][j - volumes[i]] = 1

    answer = -1
    for i in range(M + 1):
        if dp[N][i] == 1:
            answer = i

    return answer


"""
N 개의 곡, 볼륨은 M 이하, 시작 볼륨은 S
현재 볼륨이 P 일때 i 번쨰 노래는 P+V[i] 나 P-V[i] 로 연주 가능
중간에 볼륨조절 X -> 0 미만, M 초과 값만 나오는 경우 -> return -1
dp 에는 노래의 볼륨의 쵀대값이 담겨있어야 하는데 여러 값들을 어떻게 보관?
=> 답지 참고
=> dp 의 행에는 V 의 인덱스, 열에는 0 ~ M 까지 설정하고
행을 지나며 이전 행의 값 참고하여 지금 행 갱신
마지막 행에서 1의 값을 가지는 가장 큰 열의 값이 답

dp 에 어떻게 저장할 지 잘 생각하자
"""


def solution1():
    dp = [[] for _ in range(N + 1)]
    dp[0].append(S)

    for idx, volume in enumerate(volumes):
        for cur in dp[idx]:
            if 0 <= cur + volume <= M:
                dp[idx + 1].append(cur + volume)
            if 0 <= cur - volume <= M:
                dp[idx + 1].append(cur - volume)

    if not len(dp[-1]):
        return -1
    return max(dp[-1])


"""
중간에 고려했던 방식으로 구현 -> 이렇게 풀어도 됏었음
근데 메모리 초과. 지양해야 할듯
"""

print(solution1())
