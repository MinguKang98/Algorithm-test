# 1_Valid_Palindrome
import collections
import re
from typing import Deque

# 처음 코드
def isPanlindrome0(s:str)->bool:
    str_list=[]
    for i in s:
        if i.isalnum():
            str_list.append(i.lower())
    N=len(str_list)
    for j in range(N//2):
        if str_list[j]!=str_list[N-1-j]:
            return False
    return True

# solution 1 - list
def isPanlindrome1(s:str)->bool:
    str_list=[]
    for char in s:
        if char.isalnum():
            str_list.append(char.lower())
    while len(str_list)>1:
        if str_list.pop(0) != str_list.pop():
            return False
    return True

"""
시간이 더 느림 -> pop(0) 때문
list의 pop(0)는 O(n)
"""

# solution 2 - Deque
def isPanlindrome2(s:str)->bool:
    strs: Deque=collections.deque()
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    while len(strs)>1:
        if strs.popleft() != strs.pop():
            return False
    return True

"""
solution1보다 시간이 빨라짐 -> pop(0)를 popleft()로 바꾸었기 때문
deque의 popleft()는 O(1)
"""

# solution 3 - regex & slicing
def isPanlindrome3(s:str)->bool:
    s=s.lower()
    s=re.sub('[^a-z0-9]','',s)
    return s==s[::-1]

"""
정규식 공부 부족족
slicing으로 reverse까지 가능
solution 0과 solution 2보다 속도 빠름
"""

s=str(input())
print(isPanlindrome3(s))
