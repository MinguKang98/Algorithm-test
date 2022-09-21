# 56_Implement_Trie(Prefix_Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/
from collections import defaultdict

# Solution0 - mine
class TrieNode0:
    def __init__(self):
        self.val = ""
        self.child = {}


class Trie0:
    def __init__(self):
        self.root: TrieNode0 = TrieNode0()

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if not node.child.get(char):
                node.child[char] = TrieNode0()
            node = node.child.get(char)
            node.val = char
        node.child[''] = TrieNode0

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if not node or not node.child.get(char):
                return False
            node = node.child.get(char)

        if not node.child.get(''):
            return False

        return True

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if not node or not node.child.get(char):
                return False
            node = node.child.get(char)

        return True


"""
TrieNode 정의 : val - 문자, child - 문자를 key, TrieNode를 value 로 가지는 dict
오답1 ) inset apple 후, search app 은 false가 되어야 하지만 true
어떻게 구분?? -> 끝날때 무언가 -> 빈 노드가 필요 : {'', TrieNode0()}
오답2 ) 첫 글자가 다른 경우 fail
root.val을 비우고 첫 글자가 root.child에 들어가도록
"""


# Solution1 - mine
class TrieNode1:
    def __init__(self):
        self.word = False
        self.children = defaultdict(TrieNode1)
    
    """
    Solution0 와 다르게 word 값으로 bool 을 가짐
    -> 단어가 완성되면 해당 TreeNode 값이 True
    """

class Trie1:
    def __init__(self):
        self.root = TrieNode1()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node.children[char] = TrieNode1
        node.word = True
        
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.child[char]

        return node.word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.child[char]

        return True

    """
    TrieNode의 word 를 단어 완성 여부로 정의해, search와 startsWith의 코드가
    간결해짐
    defaultdict 의 사용으로 if로 체크 여부 생략 
    """

trie = Trie0()
trie.insert("apple")
print(trie.search('apple'))
print(trie.search('app'))
print(trie.startsWith('apple'))
print(trie.startsWith('app'))
