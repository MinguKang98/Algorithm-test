# 6_trip_path
# https://school.programmers.co.kr/learn/courses/30/lessons/43164
from collections import defaultdict, deque


def solution0_1(tickets):
    answer = []

    ticket_dict = defaultdict(list)
    for src, dst in tickets:
        ticket_dict[src].append(dst)

    for key in ticket_dict.keys():
        ticket_dict[key].sort(reverse=True)

    queue = deque(["ICN"])
    while queue:
        airport = queue.pop()
        answer.append(airport)
        if len(ticket_dict[airport]) == 0:
            break

        top = ticket_dict[airport].pop()
        queue.appendleft(top)

    return answer


"""
현제 공항에 대해 다음 공항이 있는지 확인
있다면 ㄱㄱ
없다면 모든 공항 갔는지 확인하고, 갔다면 종료 가지 않았다면 

처음 간 곳에 더 길이 없다면 종료됨 => backtracking 이 없어 오답
"""

answer = []
ticket_dict = defaultdict(list)
N = 0


def dfs(airport, path, depth):
    global answer, ticket_dict, N

    if depth == N:
        answer.append(path)
        return

    for node in ticket_dict[airport]:
        if not node[1]:  # 경로 있고 안갔다면
            node[1] = True
            temp = path[:]
            temp.append(node[0])
            dfs(node[0], temp, depth + 1)
            node[1] = False
    return


def solution0_2(tickets):
    global answer, ticket_dict, N

    N = len(tickets)
    for src, dst in tickets:
        ticket_dict[src].append([dst, False])

    for key in ticket_dict.keys():
        ticket_dict[key].sort()

    dfs("ICN", ["ICN"], 0)

    return answer[0]


"""
종료조건이 딱히 없어 무한루프
섬 말고 경로를 체크하는 방법은? => ticket_dict 에 넣는 값이 방문 여부 포함
dfs 를 통해 경로 탐색. 깊이가 N 이라면 중단, 현재 공항에서 갈 수 있는 공항을 순회하며 가지 않았다면 backtracking
"""


def solution1(tickets):
    ticket_dict = defaultdict(list)

    for src, dst in tickets:
        ticket_dict[src].append(dst)

    for key in ticket_dict.keys():
        ticket_dict[key].sort()

    stack = ["ICN"]
    path = []
    while stack:
        top = stack[-1]
        if ticket_dict[top]:  # 더 갈 공항 O => 스택에 다음 공항 넣기
            stack.append(ticket_dict[top].pop(0))
        else:  # 더 갈 공항 X => 현재 top 이 마지막
            path.append(stack.pop())

    return path[::-1]


"""
스택을 사용한 dfs.
스택의 top 이 현재 공항
현재 공항에서 다음 공항에 갈 수 없다면, 현재 공항은 마지막 공항.
다음 공항에 갈 수 있다면, 현재 공항을 stack 에 넣고 ticket_dict 에서 뺌
=> 다음 공항이 없다면 마지막 공항인 것을 알면 백트래킹 필요 없는듯
"""

# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]

# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]

tickets = [["ICN", "JFK"], ["ICN", "AAD"], ["JFK", "ICN"]]

print(solution1(tickets))
