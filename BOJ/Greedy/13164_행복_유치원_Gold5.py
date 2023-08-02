# 13164_행복_유치원_Gold5
# https://solved.ac/search?query=13164

N, K = map(int, input().split())
heights = list(map(int, input().split()))


def solution0():
    result = heights[N - K] - heights[0]
    for i in range(N - K, K):
        for j in range(i, 0, -1):
            temp = result - (heights[j] - heights[j - 1]) + (heights[j + 1] - heights[j])
            if result > temp:
                result = temp
            else:
                break

    return result


"""
최소의 비용 -> 조끼리 키차이의 합이 최소가 되어야 함
한명이면 가장 좋음 -> 비용 0
두명 이상이면 최대와 최소의 차가 가장 작도록
클 수록 혼자있는게 유리
오답
"""


def solution1():
    diff = [heights[i + 1] - heights[i] for i in range(N - 1)]
    diff.sort(reverse=True)
    return sum(diff[K - 1:])


"""
인접한 키들의 차를 이용
1. 인접한 키들의 차를 가지는 리스트 구함
2. 해당 리스트를 정렬
3. 작은거 부터 n-k 개 의 합 or 큰거 부터 k -1 개를 제외하고 남은 것으 합이 정답

왜 큰 거 k-1 개를 제외해야 하나? 
차를 한 개 제거하면 그룹이 두 개로 나눠짐
차를 두 개 제거하면 그룹이 세 개로 나눠짐
즉, 그룹이 K 개가 되려면 K-1 개를 제거해야 하고, 키 차이의 합이 최소가 되야 하므로 
차가 큰 것부터 K-1 개 제거하면 남은 값들의 합이 최소가 됨

차들이 큰 것부터 제거하는 문제 -> 그리디
"""

print(solution0())
