# 4_Most_Common_Word
from typing import Collection, List
import re
import collections

# 처음 코드 - 정규식만 힌트 얻음
def mostCommonWord0(paragraph: str, banned: List[str]) -> str:
    # 구두점 빼고 단어들로 list 구성
    words = [word for word in re.sub(r"[^\w]", " ", paragraph).lower().split()]
    # banned에 있는 단어 제외
    for ban in banned:
        while ban in words:
            words.remove(ban)
    # words의 word들의 개수로 이루어진 list 생성
    count = [words.count(word) for word in words]
    # count 중 가장 큰 element의 index에 해당하는 word 반환
    return words[count.index(max(count))]


# soultion1
def mostCommonWord1(paragraph: str, banned: List[str]) -> str:
    # 전처리 후 banned에 포함되지 않는 단어들로 구성된 list 생성
    words = [
        word
        for word in re.sub(r"[^\w]", " ", paragraph).lower().split()
        if word not in banned
    ]
    # 개수 들어갈 예정인 dict 생성 - defaultdict이므로 key가 없다면 추가됨
    counts = collections.defaultdict(int)
    #  word의 개수 count
    for word in words:
        counts[word] += 1
    return max(counts, key=counts.get)


"""
시간 가장 빠름
"""


# soultion2
def mostCommonWord2(paragraph: str, banned: List[str]) -> str:
    # 전처리 후 banned에 포함되지 않는 단어들로 구성된 list 생성
    words = [
        word
        for word in re.sub(r"[^\w]", " ", paragraph).lower().split()
        if word not in banned
    ]
    # words를 key, 개수를 value로 가지는 dict 생성
    counts = collections.Counter(words)
    # 가장 많은 element의 key return
    return counts.most_common(1)[0][0]


"""
빠르지만 solution1 보다는 느림
"""


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(mostCommonWord1(paragraph, banned))
