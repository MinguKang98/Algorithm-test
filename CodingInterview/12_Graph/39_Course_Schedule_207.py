# 39_Course_Schedule_207
from collections import defaultdict
from typing import List


class Solution:
    # Solution 0
    def canFinish0(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dict=defaultdict(list)
        result=[True]
        for x, y in prerequisites:
            dict[x].append(y)
    
        def dfs(start:int):

            while dict[start]:
                if dict[start][-1] in visited:
                    result.append(False)
                    return

                end=dict[start].pop()
                visited.append(end)
                dfs(end)

        visited=[]
        for key in sorted(dict.keys()):
            if key not in visited:
                visited.append(key)
                dfs(key)
        return result[-1]

    """
    cycle이 생기면 fasle, 아니라면 true
    풀이 조건을 알았지만 구현 실패
    """

     # Solution 1 - using dfs
    def canFinish1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        traced=set() # 경로 임시 저장
        
        def dfs(i): # cycle 판정 메서드 : cycle -> false , else -> true
            if i in traced: # 순환 구조이면 false
                return False
            
            traced.add(i)
            for y in graph[i]:
                if not dfs(y): #
                    return False
            traced.remove(i)

            return True

        
        for x in list(graph): # 시작점을 순회하며 cycle인지 확인
            if not dfs(x): 
                return False

        return True

    """
    Time Limit Exceeded
    """

    # Solution 2 - 가지치기
    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        traced=set() # 경로 임시 저장
        visited=set() # 방문 노드
        
        def dfs(i): # cycle 판정 메서드 : cycle -> false , else -> true
            if i in traced: # 순환 구조이면 false
                return False

            if i in visited: #  방문 했다면 cycle 아님
                return True
            
            traced.add(i)
            for y in graph[i]:
                if not dfs(y): 
                    return False
            traced.remove(i)

            visited.add(i) # 탐색 종류 후 방문 노드 추가

            return True

        
        for x in list(graph): # 시작점을 순회하며 cycle인지 확인
            if not dfs(x): 
                return False

        return True

    """
    solution 1은 모든 점을 순회하며 그 점에서 시작하는 경로를 탐색, cycle인지 판별한다.
    하지만 지나간 경로를 중복해서 탐색하므로 최적화 되지 않은 상태
    어떤 점에서 path인 상태로 탐색하다 이미 path인 노드를 만나면 그 path는 cycle이 아니라고 할 수 있다
    (ex. 1->2->3 이 path로 결정되면 5->1만 탐색해도 5에서 시작하는 path는 cycle이 아니라 할 수 있다)
    따라서 탐색이 종료되어 cycle이 아니라 판정된 시작 노드는 visited에 저장해 중복을 피한다
    """


# numCourses = 2
# prerequisites = [[1, 0]]
# prerequisites = [[1,0],[0,1]]

# numCourses = 3
# prerequisites = [[1,2], [2,0]]
# true

numCourses = 5
prerequisites = [[1,4],[2,4],[3,1],[3,2]]
# true
print(Solution().canFinish0(numCourses, prerequisites))
