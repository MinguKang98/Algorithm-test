# 4_word_changing
# https://school.programmers.co.kr/learn/courses/30/lessons/43163?language=python3
from collections import deque


def solution0(begin, target, words):
    def is_one_diff(current, word):  # for 을 사용한 방법
        cnt = 0
        for i in range(len(current)):
            if current[i] != word[i]:
                cnt += 1
        return cnt == 1

    def is_one_diff2(current, word):  # zip 을 사용한 방법
        cnt = 0
        for c, w in zip(current, word):
            if c != w:
                cnt += 1
        return cnt == 1

    answer = 0
    visited = [0 for _ in range(len(words))]

    queue = deque()
    queue.appendleft((begin, 0))
    while queue:
        cur, depth = queue.pop()
        if cur == target:
            answer = depth
            break

        for i in range(len(visited)):
            if not visited[i] and is_one_diff(cur, words[i]):
                queue.appendleft((words[i], depth + 1))
                visited[i] = 1

    return answer


"""
최소 몇단계 = 최단거리 -> bfs??
한번 가 본곳을 visit 에서 1로 처리해도 되는 이유 : 만약 다른 단어를 통해 이미 다녀온 단어가 된다 해도 그 경로는 최단거리가 될
수 없다.
"""

# begins = "hit"
# target = "cog"
# words = ["hot", "dot", "dog", "lot", "log", "cog"]

begins = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log"]

print(solution(begins, target, words))
