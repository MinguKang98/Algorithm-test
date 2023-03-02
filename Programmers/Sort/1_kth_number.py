# 1_kth_number
# https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution0(array, commands):
    answer = []
    for i, j, k in commands:
        temp_array = sorted(array[i - 1:j])
        answer.append(temp_array[k - 1])
    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution0(array, commands))
