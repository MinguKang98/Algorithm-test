# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14ABYKADACFAYh

T = 10
for _ in range(1, T + 1):
    test_case = int(input())
    data = []
    for _ in range(100):
        data.append(list(map(int, input().split())))

    start_list = [idx for idx, x in enumerate(data[0]) if x == 1]
    for start in start_list:
        visited = [[0 for _ in range(100)] for _ in range(100)]
        cur_x, cur_y = start, 0
        while cur_y < 99:
            visited[cur_y][cur_x] = 1

            if cur_x > 0 and not visited[cur_y][cur_x - 1] and data[cur_y][cur_x - 1]:
                cur_x -= 1
            elif cur_x < 99 and not visited[cur_y][cur_x + 1] and data[cur_y][cur_x + 1]:
                cur_x += 1
            else:
                cur_y += 1

        if data[cur_y][cur_x] == 2:
            print(f'#{test_case} {start}')
            break

    """
    시작점에서 찾는 법
    """

    # cur_x, cur_y = data[99].index(2), 99
    # visited = [[0 for _ in range(100)] for _ in range(100)]
    #
    # while cur_y > 0:
    #     visited[cur_y][cur_x] = 1
    #
    #     if cur_x > 0 and not visited[cur_y][cur_x - 1] and data[cur_y][cur_x - 1]:
    #         cur_x -= 1
    #     elif cur_x < 99 and not visited[cur_y][cur_x + 1] and data[cur_y][cur_x + 1]:
    #         cur_x += 1
    #     else:
    #         cur_y -= 1
    #
    # print(f'#{test_case} {cur_x}')

    """
    도착점에서 찾는 법
    방법은 맞았는데 구현이 이상했었음
    left = data[cur_y][cur_x - 1] if cur_x > 0 else 0
    right = data[cur_y][cur_x + 1] if cur_x < 99 else 0
    로 구현했던 것이 오류를 발생시킴 
    """
