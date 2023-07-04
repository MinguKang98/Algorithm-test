# 1700_멀티탭_스케줄링
# https://www.acmicpc.net/problem/1700
from collections import deque

N, K = map(int, input().split())
electrics = list(map(int, input().split()))


def solution0():
    def dfs(idx, cur_list, cur_cnt, visited_list):
        if idx == K - 1:
            answer.append(cur_cnt)
            return

        next_electric = electrics[idx + 1]
        if len(cur_list) < N:
            cur_list.append(next_electric)
            visited_list[next_electric] = 1
            dfs(idx + 1, cur_list, cur_cnt, visited_list)
        elif len(cur_list) == N:  # 멀티탭 다 찼으면
            if visited_list[next_electric]:
                dfs(idx + 1, cur_list, cur_cnt, visited_list)
            else:
                for i, electric in enumerate(cur_list):
                    remove_electric = cur_list[i]
                    visited_list[remove_electric] = 0
                    cur_list[i] = next_electric
                    visited_list[next_electric] = 1
                    dfs(idx + 1, cur_list, cur_cnt + 1, visited_list)
                    visited_list[next_electric] = 0
                    visited_list[remove_electric] = 1
                    cur_list[i] = remove_electric

    answer = []
    visited_list = [0 for _ in range(len(electrics) + 1)]
    visited_list[electrics[0]] = 1
    dfs(0, [electrics[0]], 0, visited_list)
    return min(answer)


"""
순서를 모두 알고 있음
빼는 순서를 어떻게 판단?
bfs 로 풀릴지도 => queue 에 정보 저장할 때 백트래킹 위해 값을 넣었다가 뺐는데
해당 값이 유지되지않아 실패
dfs 로 풀기 => 예제 일부 맞지만 메모리 초과 
"""


def solution1():
    plugs = []
    result = 0
    for i, electric in enumerate(electrics):
        if electric in plugs:
            continue

        if len(plugs) < N:
            plugs.append(electric)
            continue

        far_idx = 0
        temp_list = electrics[i:]
        for j, plug in enumerate(plugs):  # 꽃혀 있는 플러그 중 가장 나중에 사용되는 플러그를 찾는다
            if plug not in temp_list:  # 1번 케이스
                remove_idx = j
                break
            elif temp_list.index(plug) > far_idx:  # 2번 케이스
                far_idx = temp_list.index(plug)
                remove_idx = j

        plugs[remove_idx] = electric  # 플러그 교체
        result += 1

    return result


"""
그리디로 푸는 것을 판단 못함.  코드를 최소롤 빼려면 뒤에 나오는 순서를 모두 알아야 하는데
그리디는 뒤에 나오는 순서를 몰라야 쓴다고 혼자 판단했기 때문

뽑아야 할 플러그는 이후 상황에서 가장 나중에 사용되는 플러그
꽃혀있는 플러그들을 보며 다음을 확인 후 제거한다
1. 꽃혀있는 플러그 중 하나가 이후에 쓰이지 않으면 해당 플러그 제거
2. 꽃혀있는 플러그 모두가 이후에 쓰인다면, 가장 나중에 쓰이는 플러그를 제거

"""

print(solution1())
