# 57_Palindrome_Pairs
# https://leetcode.com/problems/palindrome-pairs/
from collections import defaultdict
from typing import List


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word_id = -1  # 단어가 끝나는 경우 index of word, 아니라면 -1
        self.palindrome_word_ids = []  # 뒤의 단어가 palindrome 일 때 add index of word


class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def insert(self, index: int, word: str) -> None:
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[0:len(word) - i]):  # word 의 남은 부분이 palindrome 인지 확인
                node.palindrome_word_ids.append(index)
            node = node.children[char]
        node.word_id = index

    def search(self, index: int, word: str) -> bool:
        result = []
        node = self.root

        while word:  # 탐색
            if node.word_id >= 0:
                if self.is_palindrome(word):    # 탐색 중간에 word != -1 and 나머지 palindrome
                    result.append([index, node.word_id])
            node = node.children[word[0]]
            word = word[1:]

        # 탐색 완료 시 word != -1
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])

        # 탐색 완료 시 palindrome_word_ids 존재
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])

        return result


class Solution:
    # Solution0 - using bruteforce
    def palindromePairs0(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(word: str) -> bool:
            start, end = 0, len(word) - 1
            while end - start > 0:
                if word[start] != word[end]:
                    return False
                start += 1
                end -= 1
            return True

        result, n = [], len(words)
        for i in range(n):
            for j in range(i + 1, n):
                test1 = words[i] + words[j]
                test2 = words[j] + words[i]
                if is_palindrome(test1):
                    result.append([i, j])
                if is_palindrome(test2):
                    result.append([j, i])
        return result

    """
    풀이는 맞지만 O(n^2)의 복잡도로 인한 Time Limit Exceeded
    """

    # Solution1 - using bruteforce
    def palindromePairs1(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(word: str) -> bool:
            return word == word[::-1]

        output = []
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i == j:
                    continue
                if is_palindrome(word1 + word2):
                    output.append([i, j])
        return output

    """
    enumerate 를 사용한 좀 더 깔끔한 풀이
    풀이는 맞지만 O(n^2)의 복잡도로 인한 Time Limit Exceeded
    """

    # Solution2 - using trie
    def palindromePairs2(self, words: List[str]) -> List[List[int]]:
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(i, word)

        results = []
        for i, word in enumerate(words):
            results.extend(trie.search(i, word))
        return results

    """
    Trie 에 reverse 한 word를 넣은 후, word를 탐색하는 방법으로 검사
    탐색해서 palindrome 을 판별할 경우는 3가지이다.
    1. 탐색이 완료되었을 때 word_id != -1
    2. 탐색이 완료되었을 때 palindrome_word_ids 존재 
    3. 탐색 중간에 word_id != -1 이고 탐색 중인 문자의 나머지 문자가 팰린드롬
    
    단어의 최대 길이를 k라고 했을 때 브루트 포스 풀이는 O(k*n^2) 이지만, 트라이를 사용하면
    O(k^2*n), 즉 O(n)으로 풀 수 있다.
    """


words = ["abcd", "dcba", "lls", "s", "sssll"]
print(Solution().palindromePairs2(words))
