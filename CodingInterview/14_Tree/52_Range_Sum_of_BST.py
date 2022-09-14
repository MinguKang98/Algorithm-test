# 52_Range_Sum_of_BST
# https://leetcode.com/problems/range-sum-of-bst/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Solution0 -using recursive dfs with pruning
    def rangeSumBST0(self, root: Optional[TreeNode], low: int, high: int) -> int:
        nums: list = []

        def search(node: TreeNode):
            if not node:
                return

            if node.val > high:
                search(node.left)
            elif node.val < low:
                search(node.right)
            else:
                nums.append(node.val)
                search(node.left)
                search(node.right)

        search(root)
        return sum(nums)

    """
    모두 탐색은 낭비 => high보다 크면 left만, low보다 작으면 right만 탐색
    """

    # Solution1 -using recursive dfs with bruteforce
    def rangeSumBST1(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        return (root.val if low <= root.val <= high else 0) \
               + self.rangeSumBST1(root.left, low, high) \
               + self.rangeSumBST1(root.right, low, high)

    """
    bruteforce => 모든 노드 탐색하므로 시간 소요 큼
    """

    # Solution2 -using recursive dfs with pruning
    def rangeSumBST2(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node: TreeNode):
            if not node:
                return 0
            if node.val < low:
                return dfs(node.right)
            elif node.val > high:
                return dfs(node.left)
            return node.val + dfs(node.left) + dfs(node.right)

        return dfs(root)

    """
    bruteforce보다 탐색 효율이 높아짐 + Solution0보다 깔끔
    """

    # Solution3 -using iterative dfs
    def rangeSumBST3(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack, sum = [root], 0
        while stack:
            node = stack.pop()
            if node:
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                if low <= node.val <= high:
                    sum += node.val
        return sum

    """
    유효한 노드만 stack에 push 하기 때문에 solution2와 유사한 탐색 구조를 가진다.
    유효한 노드 : 탐색이 필요한 노드 ex) node.val이 low보다 크면 node.left에 low보다 큰 노드가 있을 수 있다.
    """

    # Solution4 -using iterative bfs
    def rangeSumBST4(self, root: Optional[TreeNode], low: int, high: int) -> int:
        queue, sum = [root], 0
        while queue:
            node = queue.pop(0)
            if node:
                if node.val > low:
                    queue.append(node.left)
                if node.val < high:
                    queue.append(node.right)
                if low <= node.val <= high:
                    sum += node.val

        return sum
    """
    Solution3와 유사한 풀이 구조. 탐색 순서만 다르다.
    """

