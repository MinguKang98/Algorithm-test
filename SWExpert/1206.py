# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=4&pageSize=10&pageIndex=1

# import sys
#
# sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    answer = 0
    n = input()
    heights = list(map(int, input().split()))
    # n = int(sys.stdin.readline());
    # heights = list(map(int, sys.stdin.readline().split()))

    for i in range(2, n - 2):
        cur = heights[i]
        left1 = heights[i - 2]
        left2 = heights[i - 1]
        right1 = heights[i + 1]
        right2 = heights[i + 2]
        # if left1 < cur and left2 < cur and right1 < cur and right2 < cur:
        #     max_height = max(left1, left2, right1, right2)
        #     answer += cur - max_height

        max_height = max(left1, left2, right1, right2)
        if cur > max_height:
            answer += cur - max_height

    print(f"#{test_case} {answer}")
