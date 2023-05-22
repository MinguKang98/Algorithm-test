# 4_four_arithmetic_operations
# https://school.programmers.co.kr/learn/courses/30/lessons/1843

def solution0(arr):
    INF = float('inf')
    nums, ops = [], []
    for idx, element in enumerate(arr):
        nums.append(int(element)) if element % 2 == 1 else ops.append(element)

    n = len(nums)
    min_dp = [[INF for _ in range(n)] for _ in range(n)]
    max_dp = [[-INF for _ in range(n)] for _ in range(n)]

    for step in range(n):
        for start in range(n - step):
            end = start + step
            if step == 0:
                min_dp[start][start] = max_dp[start][start] = nums[start]
            else:
                for cur in range(start, end):
                    if ops[cur] == '+':
                        max_dp[start][end] = max(max_dp[start][cur] + max_dp[cur + 1][end], max_dp[start][end])
                        min_dp[start][end] = min(min_dp[start][cur] + min_dp[cur + 1][end], min_dp[start][end])
                    else:
                        max_dp[start][end] = max(max_dp[start][cur] - min_dp[cur + 1][end], max_dp[start][end])
                        min_dp[start][end] = min(min_dp[start][cur] - max_dp[cur + 1][end], min_dp[start][end])

    return max_dp[0][-1]


"""
모든 경우 구하고 최대값 찾기 => 완탐, dfs, bfs, dp 생각할 수 있을듯
괄호는 연산자 수만큼 칠 수 있음 -> 연산자 개수 : (arr-1)//2 , 숫자 개수 : (arr+1)//2
방법 못 찾아서 해설 참조

처음 생각은 연산자의 순서를 생각 => 중복을 표기할 수 없었음
연산 범위를 dp 를 통해 계산하는 것으로 이 문제를 해결할 수 있음 
1 - 3 + 5 - 8 의 경우 답은 1번째 ~ 4번째 연산의 최댓값이다.
1번째 ~ 4번째 연산의 최댓값은
1번째 ~ 1번째 연산의 최댓값 - 2번째 ~ 4번째 연산의 최솟값
1번째 ~ 2번째 연산의 최댓값 + 3번째 ~ 4번째 연산의 최댓값
1번째 ~ 3번째 연산의 최댓값 - 4번째 ~ 4번째 연산의 최소값
중 가장 큰 값이다.  이런식으로 구간에 따른 연산의 최댓값 최솟값을 저장하여 다음 연산에 사용하는 식으로 해결해야한다.

필요한 변수는 최솟값을 저장하는 min_dp, 최댓값을 저장하는 max_dp이다.
min_dp[i][j] 와 max_dp[i][j] 는 각각 i번째부터 j번째까지 구간의 연산의 최솟값, 최댓값을 저장한다.
최종적으로 max_dp[0][n-1] 을 구해야 하므로 [n-1][n-1] 부터 위로 올라가며 계산한다.

참고
https://school.programmers.co.kr/questions/35224
https://school.programmers.co.kr/questions/48711
"""

arr = ["1", "-", "3", "+", "5", "-", "8"]
print(solution0(arr))
