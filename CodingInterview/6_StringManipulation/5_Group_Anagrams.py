# 5_Group_Anagrams
from typing import List
import collections

# solution
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)
    for str in strs:
        # 단어 정렬 후 애너그램을 key로 하는 dictionary에 넣어줌
        anagrams["".join(sorted(str))].append(str)
    return list(anagrams.values())


"""
정렬 힌트받음
같은 anagram가지는 단어끼리 dict에 넣는 것은 생각했지만 구현 미숙하여 해설참조
"""


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
