# 2_Reverse_String
from typing import List
import sys

# 처음코드
def reverseString0(s: List[str]) -> None:
    s.reverse()
    print(s)

# solution 1 - 투 포인터(mine)
def reverseString1(s: List[str]) -> None:
    n=len(s)
    for i in range(n//2):
        s[i],s[n-i-1]=s[n-i-1],s[i]
    print(s)

# solution 1 - 투 포인터(sol)
def reverseString1_1(s: List[str]) -> None:
    left,right=0,len(s)-1
    while left<right:
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
    print(s)
    
"""
가장 시간 느림
"""

# solution 2 - 문자열 슬라이싱
def reverseString2(s: List[str]) -> None:
    s=s[::-1]
    # s[:]=s[::-1] 
    # 위의 코드가 오류일때 사용하는 트릭
    print(s)

"""
가장 시간 빠름
"""

command=list(sys.stdin.readline().rstrip())
reverseString1_1(command)