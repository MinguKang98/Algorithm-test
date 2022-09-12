# 50_Convert_Sorted_Array_to_Binary_Search_Tree
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # Solution0 - using dfs
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(sub_nums: List[int]) -> TreeNode:
            idx = len(sub_nums) // 2
            root = TreeNode(sub_nums[idx])
            left_nums, right_nums = sub_nums[:idx], sub_nums[idx + 1:]
            if len(left_nums) != 0:
                root.left = dfs(left_nums)
            if len(right_nums) != 0:
                root.right = dfs(right_nums)

            return root

        return dfs(nums)

    """
    dfs로 무엇을 return? list를 받아 BST 형태의 TreeNode를 return 
    """

    # Solution1 - using devide and conquer
    def sortedArrayToBST1(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid = len(nums) // 2

        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST1(nums[:mid])
        node.right = self.sortedArrayToBST1(nums[mid + 1:])

        return node

    """
    로직은 같지만 코드가 살짝 다르다.
    """
