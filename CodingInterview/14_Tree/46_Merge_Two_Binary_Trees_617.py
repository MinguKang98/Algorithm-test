# 46_Merge_Two_Binary_Trees_617
# https://leetcode.com/problems/merge-two-binary-trees/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Solution0 - using dfs
    def mergeTrees0(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node1: TreeNode, node2: TreeNode):
            node = TreeNode()
            if node1 and node2:
                node.val = node1.val + node2.val
                node.left = dfs(node1.left, node2.left)
                node.right = dfs(node1.right, node2.right)
            elif not node1 and node2:
                node.val = node2.val
                node.left = dfs(None, node2.left)
                node.right = dfs(None, node2.right)
            elif node1 and not node2:
                node.val = node1.val
                node.left = dfs(node1.left, None)
                node.right = dfs(node1.right, None)
            else:
                return None

            return node

        return dfs(root1, root2)

    # Solution1 - using recursive dfs
    def mergeTrees1(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees1(root1.left, root2.left)
            node.right = self.mergeTrees1(root1.right, root2.right)
            return node
        else:
            return root1 or root2

    """
    root1, root2 의 경우를 모두 구분한 solution0 와 달리 solution1은 모두 존재하는 경우만 연산하고 나머지 경우는
    return root1 or root2 를 사용하여 코드를 단순화함
    """
