# 6_enforcement_camera
# https://school.programmers.co.kr/learn/courses/30/lessons/42884


def solution0(routes):
    routes.sort()
    answer = 1
    point = routes[0][1]
    for start, end in routes[1:]:
        if start <= point <= end:
            continue
        elif end < point:
            point = end
        else:
            point = end
            answer += 1
    return answer


"""
routes 를 들어온 지점을 기준으로 정렬한다.
처음 카메라 설치 지점은 차량의 나간 지점
routes 를 순회하며 차량의 나간 지점이 이동 경로에 포함되어 있는지 확인
포함된다면 갯수 유지, 카메라 설치 지점 유지
포함 안되면 갯수 하나 추가, 카메라 설치 지점 변경 
=> 오답. 이전 경로가 다음 경로를 포함할 때를 고려 안한듯 함. 
이전 경로가 다음 경로 포함하면 카메라 설치 지점을 차량 나간 지점으로 변경
=> 정답
"""


def solution1(routes):
    routes.sort(key=lambda x: x[1])
    last_camera = -30001
    answer = 0

    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]
    return answer


"""
routes 를 나간 지점을 기준으로 정렬한다.
마지막 카메라가 차량 들어온 지점보다 뒤에 있다면, 차량 나간 지점에 카메라를 추가한다.
"""

# routes = [[-20, -15], [-14, -5], [-18, -13], [-5, -3]]

routes = [[-100, 100], [50, 170], [150, 200], [-50, -10], [10, 20], [30, 40]]

print(solution0(routes))
