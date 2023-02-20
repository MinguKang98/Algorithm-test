# 3_making_big_number
# https://school.programmers.co.kr/learn/courses/30/lessons/42883

def solution0(number, k):
    answer = []
    idx = 0
    while len(answer) < len(number) - k:
        temp_num = int(number[idx])
        temp_idx = idx
        for j in range(idx + 1, k + 1 + len(answer)):
            num = int(number[j])
            if temp_num < num:
                temp_num = num
                temp_idx = j
                if num == 9:
                    break;

        answer.append(temp_num)
        idx = temp_idx + 1

    return ''.join(map(str, answer))


"""
전체 길이 - k 까지 중에서 가장 큰 수 찾은 후 뒤에서도 같은 작업
=> 8, 10 시간초과
힌트) 9 만나면 가장 큰값이므로 탐색 중지
=> 10 시간초과
=> 왜?? 위와 같이 풀면 탐색했던 부분을 또 탐색하게 됨. 수가 커질 때 시간초과를 유발하므로 다른 방법을 찾자
"""


def solution1(number, k):
    stack = []
    for num in number:
        while stack and k > 0 and stack[-1] < num:  # 아직 뺄 수 있다면 (num 이 top 보다 크고, stack 이 비지 않으며, k >0)
            stack.pop()
            k -= 1
        stack.append(num)
    stack = stack[:-k] if k > 0 else stack  # stack 의 길이가 k 이상이면 자르기
    return ''.join(stack)


"""
앞자리가 클수록 큰 수이므로 number 의 앞에서 부터 탐색하며 비교적 작은 수를 k 개 뺀다.
num 이 stack 의 top 보다 크다면 top 을 제거하고 (제가하는 수) num 을 넣는다.

남는 것을 중심으로 생각했는데, 빼는 것을 중심으로 생각하니 더 편한 것 같음
"""

# number = "1924"
# k = 2

# number = "1231234"
# k = 3

number = "4177252841"
k = 4

print(solution1(number, k))
