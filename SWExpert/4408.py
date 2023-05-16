# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&contestProbId=AWNcJ2sapZMDFAV8&categoryId=AWNcJ2sapZMDFAV8&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=PYTHON&select-1=4&pageSize=10&pageIndex=1
from collections import defaultdict

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    move_dict = defaultdict(list)
    answer = 0
    for _ in range(n):
        src, dst = map(int, input().split())
        src = (src + 1) // 2
        dst = (dst + 1) // 2
        if src > dst:
            src, dst = dst, src
        elif src == dst:
            continue
        move_dict[src].append(dst)

    for key in move_dict.keys():
        move_dict[key].sort()

    while move_dict:
        temp_src = min(move_dict.keys())
        while True:
            temp_dst = move_dict[temp_src].pop(0)
            if not move_dict[temp_src]:
                move_dict.pop(temp_src)
            temp_list = [k for k in move_dict.keys() if k > temp_dst]
            if not temp_list:
                break
            temp_src = min(temp_list)

        answer += 1
    print(f'#{test_case} {answer}')

"""
move_dict 를 앞부터 순회하며 가장 많이 들어 가도록 하게 함
=> 오답 : 큰 번호에서 작은 번호로 가는 거 고려 안함
앞에서 뒤로 가나 뒤에서 앞으로 가나 차지하는 범위는 같음 => move_dict 구성만 다르게
1->3, 4->6 일 경우 겹치는데 안겹친다고 생각하여 오담.  
"""
