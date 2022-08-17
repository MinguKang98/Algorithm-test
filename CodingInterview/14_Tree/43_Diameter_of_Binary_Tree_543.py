# 43_Diameter_of_Binary_Tree_543
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Solution0_1 - using dfs : fail
    def diameterOfBinaryTree0_1(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            left_depth, right_depth = 1, 1

            if node.left is not None:
                left_depth = dfs(node.left) + 1
            if node.right is not None:
                right_depth = dfs(node.right) + 1

            return max(left_depth, right_depth)

        return dfs(root.left) + dfs(root.right)

    """
    테스트 케이스 대부분 통과 but 오답 -> 최장 경로에 루트가 없는 경우 생각 못해서
    dfs로 무엇을 return? 리프 노드에서 현재 노드까지의 최장 거리
    """

    # Solution0_2 - using dfs
    def diameterOfBinaryTree0_2(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]):  # (최대 길이, 최대 경로 길이)
            if node is None:
                return 0, 0
            left_len, right_len = 0, 0
            left_max, right_max = 0, 0

            if node.left is not None:
                left_node = dfs(node.left)
                left_len = left_node[0] + 1
                left_max = left_node[1]
            if node.right is not None:
                right_node = dfs(node.right)
                right_len = right_node[0] + 1
                right_max = right_node[1]

            return max(left_len, right_len), max(left_max, right_max, left_len + right_len)

        return dfs(root)[1]

    """
    최장 경로에 루트가 없는 경우를 고려 -> 자식들을 이은 길이(left_len + right_len + 2) 와
    자식들이 가지는 최장 거리(left_max, right_max)를 비교하기로 설계
    dfs로 무엇을 return? 리프 노드에서 현재 노드까지 최장 거리 & 최장 경로
    """

    # Solution1 - using dfs
    longest: int = 0

    def diameterOfBinaryTree1(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left + right + 2)
            return max(left, right) + 1

        dfs(root)
        return self.longest

    """
    Solution0_2와 방법은 같지만 더 깔끔한 풀이
    
    dfs로 무엇을 return? 리프 노드에서 현재 노드까지의 최장 거리
    최장 경로는 longest 라는 변수 사용해서 저장
    """
