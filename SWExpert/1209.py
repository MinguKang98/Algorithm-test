# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&contestProbId=AV13_BWKACUCFAYh&categoryId=AV13_BWKACUCFAYh&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=PYTHON&select-1=4&pageSize=10&pageIndex=1

T = 10
for _ in range(1, T + 1):
    test_case = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    temp = []
    for j in range(100):
        temp.append(sum(data[j]))

    for i in range(100):
        temp.append(sum([data[x][i] for x in range(100)]))

    temp.append(sum(data[x][x] for x in range(100)))
    temp.append(sum(data[x][99 - x] for x in range(100)))

    print(f'#{test_case} {max(temp)}')
