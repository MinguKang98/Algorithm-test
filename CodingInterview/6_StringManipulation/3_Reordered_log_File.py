# 3_Reordered_log_File
from typing import List

# solution
"""
첫 시도에 digit와 letter을 구별해야 하고 정렬 시 lambda key를 쓰는것
까지는 파악했으나 log들을 실제로 나누는 것을 파악 못해 진행이 더
되지 않아 솔루션 참조
"""


def reorderLogFiles(logs: List[str]) -> List[str]:
    # 로그 들을 letter과 digit으로 나누어줌
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    # letters는 문자 순, 동일하면 식별자 순
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    # digits는 입력 순이므로 변경 x
    return letters + digits


logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
print(reorderLogFiles(logs))
