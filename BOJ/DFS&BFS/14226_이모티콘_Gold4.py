# 14226_이모티콘_Gold4
# https://www.acmicpc.net/problem/14226
from collections import deque

S = int(input())


def solution():
    visited = [[0 for _ in range(1001)] for _ in range(1001)]
    queue = deque()
    queue.appendleft((1, 0, 0))  # 개수, 클립보드, 시간
    visited[0][1] = 1  # 클립, 개수

    while queue:
        cnt, clip, time = queue.pop()

        if cnt == S:
            return time

        if 0 <= cnt <= 1000:  # 복사
            if not visited[cnt][cnt]:
                visited[cnt][cnt] = 1
                queue.appendleft((cnt, cnt, time + 1))

        if 0 <= cnt + clip <= 1000 and 0 < clip <= 1000:  # 붙여넣기
            if not visited[clip][cnt + clip]:
                visited[clip][cnt + clip] = 1
                queue.appendleft((cnt + clip, clip, time + 1))

        if 0 <= cnt - 1 <= 1000 and 0 <= clip <= 1000:  # 제거
            if not visited[clip][cnt - 1]:
                visited[clip][cnt - 1] = 1
                queue.appendleft((cnt - 1, clip, time + 1))


"""
모두 복사, 붙여넣기, 하나 삭제
시간의 최솟값 -> 그래프로 풀면 bfs 가능
최소값이므로 처음 도착한 개수에는 다시 안가도 됨
=> 오답
=> 개수 같아도 클립수 다르면 다른 결과 => visited 를 클립수 X 개수 인 2차원으로
=> 정답

visited 의 기본값을 -1 로 하고 누적되도록 하면 시간을 저장 가능
"""

print(solution())
