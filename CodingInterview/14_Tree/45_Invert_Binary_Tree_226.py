# 45_Invert_Binary_Tree_226
# https://leetcode.com/problems/invert-binary-tree/
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Solution0 -using dfs
    def invertTree0(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: TreeNode):
            if not node:
                return

            node.left, node.right = dfs(node.right), dfs(node.left)
            return node

        return dfs(root)

    """
    dfs를 사용하여 node 전환
    dfs로 무엇을 return? 반전된 TreeNode의 root
    """

    # Solution1 - pythonic
    def invertTree1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree1(root.right), self.invertTree1(root.left),
            return root
        return None

    # Solution2 - using iterative bfs
    def invertTree2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)

        return root

    """
    queue를 사용한 bfs. top-down 방식으로 노드를 반전
    """

    # Solution3 - using iterative pre-order dfs
    def invertTree3(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = deque([root])

        while stack:
            node = stack.pop()

            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)
        
        return root
    
    """
    stack을 사용한 bfs. tree의 오른쪽 부터 반전시킨다.
    """

    # Solution4 - using iterative post-order dfs
    def invertTree4(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = deque([root])

        while stack:
            node = stack.pop()

            if node:
                stack.append(node.left)
                stack.append(node.right)

                node.left, node.right = node.right, node.left

        return root

    """
    Solution3와 같지만, 탐색 순서가 달라진다. 
    """
