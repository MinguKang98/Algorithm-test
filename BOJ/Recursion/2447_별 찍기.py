# 2447_별 찍기 - 10

# 별을 출력
def star1(N):
    if N == 3:  # 가장 작은 3X3 정사각형
        star_list[0][:3] = star_list[2][:3] = ["*"] * 3
        star_list[1] = ["*", " ", "*"]
        return
    else:
        a = N // 3
        star1(N // 3)  # 재귀 - 나머지 패턴들을 채워 올 것
        # 큰 3x3 정사각형 모양에서
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:  # 가운데는 별 넣지 않음
                    continue
                for k in range(a):  # 나머지 칸은 한 단계 작은 3X3 정사각형((0,0)에 존재) 복사
                    star_list[a * i + k][a * j : a * (j + 1)] = star_list[k][:a]


# 같은 알고리즘이지만 간단 & 빠름
def star2(N):
    if N == 1:
        return ["*"]

    stars = star2(N // 3)  # 이전 단계 3X3 정사각형 가져옴
    result = []

    for s in stars:  # 첫째줄 복사
        result.append(s * 3)
    for s in stars:  # 둘째줄 복사 & 가운데는 비어있음
        result.append(s + " " * (N // 3) + s)
    for s in stars:  # 셋째줄 복사
        result.append(s * 3)

    return result


N = int(input())  # N은 3^k
# star_list = [[" "] * N for _ in range(N)]
# star1(N)
# for i in range(N):
#    for j in range(N):
#        print(star_list[i][j], end="")
#    print()
print("\n".join(star2(N)))


"""
무엇을 재귀?? 별 입력을 재귀. 3X3 정사각형에서 가운데를 뺀 8개 정사각형에
                한단계 낮은 정사각형을 복사
언제 종료?? n=3일때 / n=1일때 종료
"""
