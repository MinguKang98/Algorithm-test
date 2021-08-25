# 9251_LCS.py

# DP 2-dimenstion list
def LCS(string_list):
    arr = [[0] * 1000 for _ in range(1000)]
    N = len(string_list[0])
    M = len(string_list[1])
    for i in range(N):
        for j in range(M):
            # 추가된 글자가 같다면 이전 substring+1
            if string_list[0][i] == string_list[1][j]:
                arr[i][j] = arr[i - 1][j - 1] + 1
            # 다르다면 이전 substring들 중 max값
            else:
                arr[i][j] = max(arr[i][j - 1], arr[i - 1][j])
    return arr[-1][-1]


# DP 1-dimenstion list
def LCS2(string_list):
    arr = [0] * 1000
    N = len(string_list[0])
    M = len(string_list[1])
    for i in range(N):
        max_temp = 0
        for j in range(M):
            if max_temp < arr[j]:
                max_temp = arr[j]
            elif string_list[0][i] == string_list[1][j]:
                arr[j] = max_temp + 1
    return max(arr)


if __name__ == "__main__":
    string_list = []
    for _ in range(2):
        string_list.append(input())
    print(LCS2(string_list))

"""
풀이방법

"""
