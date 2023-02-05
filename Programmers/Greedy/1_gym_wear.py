# 1_gym_wear
# https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution0(n, lost, reserve):
    answer = 0
    wear_list = [1 for _ in range(n)]
    for l in lost:
        wear_list[l - 1] -= 1

    for r in reserve:
        wear_list[r - 1] += 1

    for idx, wear in enumerate(wear_list):
        pre, next = max(0, idx - 1), min(n - 1, idx + 1)
        if wear == 0:
            if wear_list[pre] == 2 and wear_list[next] == 2:
                wear_list[pre] -= 1
                answer += 1
            elif wear_list[pre] == 2 and wear_list[next] != 2:
                wear_list[pre] -= 1
                answer += 1
            elif wear_list[pre] != 2 and wear_list[next] == 2:
                wear_list[next] -= 1
                answer += 1
        else:
            answer += 1

    return answer


"""
lost 와 reserve 를 사용해 가지고 있는 옷의 개수를 나타내는 wear_list 생성
현재 0 벌인 학생은 2 벌인 앞이나 뒤 학생한테 빌릴 수 있음. 만약 앞 뒤 모두 두 벌이면 뒤 학생한테 빌려야 
현재 answer 의 값이 체육 수업을 들을 수 있는 학생의 최댓값이 됨
"""


def solution1(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]  # 두 벌인 학생
    _lost = [l for l in lost if l not in reserve]  # 0 벌인 학생
    _reserve.sort()

    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)

    return n - len(_lost)


"""
두 벌인 학생의 앞(f) 뒤(b) 에 0 벌인 학생이 있다면 _lost.remove 로 _lost 에서 제외
_reserve 의 loop 가 끝나면 _lost 에는 옷을 못 빌려 아직 0 벌인 학생들만 남으므로 체육수업을 들을 수 
있는 학생의 최댓값은 n - len(_lost)  
참고로, 앞뒤 모두 0벌이면 앞의 학생을 먼저 처리함 
"""

n = 5
lost = [2, 4]
reserve = [1, 3, 5]

# n = 5
# lost = [2, 4]
# reserve = [3]

# n = 3
# lost = [3]
# reserve = [1]

print(solution0(n, lost, reserve))
