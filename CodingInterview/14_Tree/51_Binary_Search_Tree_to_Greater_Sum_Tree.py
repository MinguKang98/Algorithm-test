# 51_Binary_Search_Tree_to_Greater_Sum_Tree
# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    val: int = 0
    # Solution0 - using
    def bstToGst0(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        node = TreeNode(root.val)
        node.right = self.bstToGst0(root.right)
        self.val += node.val
        node.val = self.val
        node.left = self.bstToGst0(root.left)
        return node

    """
    dfs => 현재 값보다 더 큰 값을 가진 노드 합
    큰 값들 먼저 계산해야함 : right -> mid -> left 순서로 순회
    처음에는 node.val에 node.right.val을 더하고, node.left.val 에 node.val을 더했으나 오류
    => 해당 노드보다 큰 값을 더한다는 보장이 없음 + left 계산 오류
    누적값을 선언 후 트리를 순회하며 누적값 갱신, node.val에 더함 => 해당 노드보다 큰 값들의 합 보장    
    """

    # Solution1 - using in-order traversal
    def bstToGst1(self, root: TreeNode) -> TreeNode:
        if root:
            self.bstToGst1(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst1(root.left)
        return root

    """
    Solution0는 새로운 노드를 생성하지만 Solution1은 기존 노드의 값만 갱신
    """
