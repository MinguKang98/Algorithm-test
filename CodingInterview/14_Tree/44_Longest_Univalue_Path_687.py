# 44_Longest_Univalue_Path_687
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    longest: int = 0

    # Solution0 - using dfs
    def longestUnivaluePath0(self, root: Optional[TreeNode]) -> int:

        def dfs(node: TreeNode):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            result = 0
            if node.left and node.val == node.left.val:
                left += 1
                result += (left + 1)
            if node.right and node.val == node.right.val:
                right += 1
                result += (right + 1)
            self.longest = max(left, right, result)
            return max(left, right)

        dfs(root)
        return self.longest

    """
    dfs로 무엇을 return? 리프 노드에서 현재 노드까지 최장 거리
    최장 길이는 변수로 처리
    오답 -> child node의 val과 parent node의 val이 다르면 left와 right값은 0으로 처리해주어야함
    (연결이 끊기므로 left, right의 의미 상실) -> 하지 않아 오답
    """

    # Solution1 - using dfs
    def longestUnivaluePath1(self, root: Optional[TreeNode]) -> int:

        def dfs(node: TreeNode):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            if node.left and node.val == node.left.val:
                left += 1
            else:
                left = 0
            if node.right and node.val == node.right.val:
                right += 1
            else:
                right = 0
            self.longest = max(left + right, self.longest)
            return max(left, right)

        dfs(root)
        return self.longest
    """
    Solution0에서 하지 않은 child node의 val과 parent node의 val이 다르면 left와 right값은 0으로 처리
    """