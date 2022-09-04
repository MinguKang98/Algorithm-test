# 48_Balanced_Binary_Tree
# https://leetcode.com/problems/balanced-binary-tree/
import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # Solution0 -using dfs
    def isBalanced0(self, root: Optional[TreeNode]) -> bool:
        self.maximum = -sys.maxsize

        def dfs(node: TreeNode):
            if not node:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)
            self.maximum = max(abs(left - right), self.maximum)
            return max(left, right) + 1

        dfs(root)
        if self.maximum <= 1:
            return True
        else:
            return False

    """
    dfs가 무엇을 return? 노드의 깊이, 서브 노드 깊이의 차의 최댓값을 변수로 설정 후 갱신
    """

    # Solution1 -using recursive dfs
    def isBalanced1(self, root: Optional[TreeNode]) -> bool:
        def check(node: TreeNode):
            if not node:
                return 0

            left = check(node.left)
            right = check(node.right)

            if left == - 1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return check(root) != -1

    """
    dfs가 무엇을 return? 노드의 깊이, solution0와 달리 left와 right의 깊이 차가 1이하 일때만
    노드의 깊이를 return하고, 차가 1보다 크면 -1을 return 한다. 
    따라서 함수의 return 값이 -1과 일치하는지 비교하면 된다.
    """
