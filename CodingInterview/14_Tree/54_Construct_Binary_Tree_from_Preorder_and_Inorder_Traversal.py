# 54_Construct_Binary_Tree_from_Preorder_and_Inorder_Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Solution0 -using recursive dfs with in-order traversal
    def buildTree0(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None
        root_idx = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        left_inorder, right_inorder, = inorder[:root_idx], inorder[root_idx + 1:]
        n = len(left_inorder)
        left_preorder, right_preorder = preorder[1:n + 1], preorder[n + 1:]
        root.left = self.buildTree0(left_preorder, left_inorder)
        root.right = self.buildTree0(right_preorder, right_inorder)

        return root

    """
    preorder[0] -> root, inorder 에서 root의 index 찾음
    root index 기준으로 inorder의 left, right 구분
    inorder의 left, right의 길이를 사용해서 preorder의 left, right 구분
    root를 사용해 노드 만든 후, sub inorder 과 sub preorder 를 사용해서 dfs
    dfs의 결과값을 root의 left, right로 설정
    """

    # Solution1 - using divide and conquer
    def buildTree1(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            index = inorder.index(preorder.pop(0))

            node = TreeNode(inorder[index])
            node.left = self.buildTree1(preorder, inorder[:index])
            node.right = self.buildTree1(preorder, inorder[index + 1:])

            return node

    """
    Solution1 처럼 전위 순회 시 preorder[0]는 항상 root 가 된다.
    pop(0) 를 수행한 preorder 과 slicing 한 inorder 를 dfs
    """
