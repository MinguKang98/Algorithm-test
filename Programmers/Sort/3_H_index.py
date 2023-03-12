# 3_H_index
# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution0(citations):
    answer = len(citations)
    citations.sort()
    for citation in citations:
        if citation >= answer:
            break
        answer -= 1

    return answer


"""
n 편 중 h 번 이상 인용된 논문이 h 편 이상, 나머지는 h 편 이하라면 h 의 최대값이 H-index
H-index 의 값은 길이보다 클 수 없다. H-index 의 값을 len(citations) 로 설정하고 citations 를 오름차순 정렬 후,
앞에서 부터 H-index 의 값을 줄여가며 답을 찾는다.
"""


def solution1(citations):
    answer = 0
    citations.sort(reverse=True)
    for citation in citations:
        if citation > answer:
            answer += 1
    return answer


"""
solution0 을 거꾸로 한 풀이이다. 
"""

citations = [3, 0, 6, 1, 5]

print(solution0(citations))
