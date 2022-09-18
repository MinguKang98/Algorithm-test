# 53_Minimum_Distance_Between_BST_Nodes
# https://leetcode.com/problems/minimum-distance-between-bst-nodes
import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    prev: int = -sys.maxsize
    result: int = sys.maxsize

    # Solution 1 - using recursive dfs with in-order traversal
    def minDiffInBST1(self, root: Optional[TreeNode]) -> int:
        if root.left:
            self.minDiffInBST1(root.left)

        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.minDiffInBST1(root.right)

        return self.result

    """
    root 노드와 가장 작은 후보 노드 -> left 중 가장 right & right 중 가장 left
    이런한 동작 수행하기 위해 중위 순회 + 이전 탐색 노드와 현재 노드 비교
    """

    # Solution 2 - using iterative dfs with in-order traversal
    def minDiffInBST2(self, root: Optional[TreeNode]) -> int:
        prev: int = -sys.maxsize
        result: int = sys.maxsize

        stack = []
        node = root

        while stack or node:
            while node:  # left 끝까지 탐색
                stack.append(node)
                node = node.left

            node = stack.pop()

            result = min(result, node.val - prev)
            prev = node.val

            node = node.right

        return result
    
    """
    Solution1을 반복 구조로 바꾼 풀이. 동작은 일치함
    """
