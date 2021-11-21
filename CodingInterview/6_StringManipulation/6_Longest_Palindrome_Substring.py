# 6_Longest_Palindrome_Substring

# 처음 코드
def longestPalindrome0(s: str) -> str:
    lps = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            subs = s[i:j]
            if len(subs) < 2 or subs == subs[::-1]:
                lps.append(subs)
    return max(lps, key=len)


"""
Time Limit Exceeded - O(n^2)
"""

# solution 1 - two pointer
def longestPalindrome1(s: str) -> str:
    def expand(left: int, right: int) -> str:
        # s의 left와 right가 같다면 양 옆으로 확장
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ""
    for i in range(0, len(s) - 1):
        # result, 짝수 포인터, 홀수 포인터 중 가장 길이 긴 것이 result
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
    return result


"""
양 끝이 같을때 비교하는 것을 생각하긴 했지만 그냥 넘어감
"""

# solution 2-1 - dynamic programming
def longestPalindrome2(s: str) -> str:
    N = len(s)
    dp = [[0] * N for _ in range(N)]

    result = []
    # 포인터 left와 right를 기준으로
    for i in range(N):  # substr의 길이 1
        dp[i][i] = 1
        result.append(s[i])
    for left in range(N - 1):  # substr의 길이 2 이상
        for right in range(left + 1, N):
            print(f"s[{left}:{right+1}] : {s[left : right + 1]}")
            if s[left] == s[right]:
                if dp[left + 1][right - 1] or right == left + 1:
                    dp[left][right] = 1
                    result.append(s[left : right + 1])
                    print(s[left : right + 1])

    return max(result, key=len)


"""
dp를 하기위한 이전 것들이 계산되지 않는 상황이 나옴
ex) dp[0][3]을 위해 dp[1][2]가 필요하지만 계산되지 않았다
"""

# solution 2-2 - dynamic programming
def longestPalindrome3(s: str) -> str:
    N = len(s)
    dp = [[0] * N for _ in range(N)]

    result = []
    # substr의 length를 기준으로
    for length in range(1, N + 1):
        for left in range(N - length + 1):
            right = left + length - 1
            if left == right:  # substr의 길이 1
                dp[left][right] = 1
                result.append(s[left : right + 1])
            elif s[left] == s[right]:
                if dp[left + 1][right - 1] or right == left + 1:  # substr의 길이 2 or 3이상
                    dp[left][right] = 1
                    result.append(s[left : right + 1])
    return max(result, key=len)


"""
시간 많이 걸림
"""

# s = "babad"
# s = "cbbd"
s = "aaaa"
print(longestPalindrome2(s))
