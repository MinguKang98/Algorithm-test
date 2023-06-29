# 2504_괄호의_값_Silver1
# https://www.acmicpc.net/problem/2504

signs = input()
stack = []
answer = 0
temp = 1

for idx, sign in enumerate(signs):
    if sign == '(':
        stack.append(sign)
        temp *= 2

    elif sign == '[':
        stack.append(sign)
        temp *= 3

    elif sign == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        if signs[idx - 1] == '(':  # () 가 제일 안쪽의 괄호일 때 더해줌
            answer += temp
        stack.pop()
        temp //= 2  # 이전 temp 로 돌아가도록 함

    else:  # sign == ']'
        if not stack or stack[-1] == '(':
            answer = 0
            break
        if signs[idx - 1] == '[':
            answer += temp
        stack.pop()
        temp //= 3

if stack:
    print(0)
else:
    print(answer)

"""
스택을 쓰는 듯
1. 올바른 괄호쌍인지 판단
2. 안에 있으면 곱하고 옆에 있으면 더함
숫자 어떻게?? => 숫자를 스택에 넣는 방식을 썼는데 숫자 처리가 너무 복잡함 + 오류 나옴

풀이들 참조 => 계산하는 값들을 보관하는 temp 와 정답인 answer 를 사용하여 풀이
괄호를 시작할 때 temp 에 2 or 3 을 곱해줌
괄호를 닫을 때 invalid 하다면 answer = 0 후 break
만약 현재의 괄호가 이전의 괄호와 쌍이라면 answer += temp, 즉 결합되지 않은 괄호일 때의
값을 ansewr 에 더한다
이때 stack 의 top 이 아닌 이전 괄호인 이유는 결합되지 않은 괄호일 때 한번만 더해줘야 하기 때문이다
이후 stack.pop() 하고 temp 를 2 or 3 으로 나눠 결합되지 않은 괄호일 때 temp 값으로
되돌린다

숫자 처리에서 어려움 느낌
"""
