# 5_new_clustering
# https://school.programmers.co.kr/learn/courses/30/lessons/17677
from collections import Counter
import re


class Solution:
    def new_clustering0(self, str1: str, str2: str):
        str1 = str1.upper()
        str2 = str2.upper()

        # 부분집합 A, B 와 교집합 구하기
        A, B = [], []
        intersection = 0

        for i in range(len(str1) - 1):
            suba = str1[i:i + 2]
            if suba.isalpha():
                A.append(suba)
        a = len(A)

        for i in range(len(str2) - 1):
            subb = str2[i:i + 2]
            if subb.isalpha():
                B.append(subb)
                if subb in A:
                    intersection += 1
                    A.remove(subb)

        # 합집합 구하기 : (A - B) + B
        union = a - intersection + len(B)

        if union == 0:
            return 65536

        return int(intersection / union * 65536)

    """
    교집합의 갯수는 부분집합 B 구하는 증에 세도록 함.
    합집합을 따로 구하는 것이 아닌 len(A) + len(B) - intersection 으로 계산 
    """

    def new_clustering1(self, str1: str, str2: str):
        str1s = [str1[i:i + 2].lower() for i in range(len(str1) - 1)
                 if re.findall('[a-z]{2}', str1[i:i + 2].lower())]

        str2s = [str2[i:i + 2].lower() for i in range(len(str2) - 1)
                 if re.findall('[a-z]{2}', str2[i:i + 2].lower())]

        intersection = sum((Counter(str1s) & Counter(str2s)).values())
        union = sum((Counter(str1s) | Counter(str2s)).values())

        jaccard_sim = 1 if union == 0 else intersection / union
        return int(jaccard_sim * 65536)

    """
    우선 부분집합을 구하는 코드가 더 pythonic 함. isalpha() 가 아닌 정규식을 사용
    intersection 과 union 은 multiset 임. python 은 multiset 을 지원하지 않음
    Counter 와 &, | 를 사용하여 교집합, 합집합을 구할 수 있음
    """


str1 = 'FRANCE'
str2 = 'french'

# str1 = 'handshake'
# str2 = 'shake hands'

# str1 = 'aa1+aa2'
# str2 = 'AAAA12'

# str1 = 'E=M*C^2'
# str2 = 'e=m*c^2'

print(Solution().new_clustering1(str1, str2))
