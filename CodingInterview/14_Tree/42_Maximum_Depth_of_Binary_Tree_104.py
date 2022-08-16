# 42_Maximum_Depth_of_Binary_Tree_104
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Solution0 - using bfs
    def maxDepth0(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = [(root, 1)]
        depth = 1
        while queue:
            node, count = queue.pop(0)
            depth = max(depth, count)
            left_node, right_node = node.left, node.right
            if left_node is not None:
                queue.append((left_node, count + 1))
            if right_node is not None:
                queue.append((right_node, count + 1))
        return depth

    """
    node 마다 수행 -> node 마다 depth가 일정하지 않음 -> node와 함꼐 depth 추가 & 초기 None case 추가
    -> 기존 depth와 현재 count를 비교하여 전체 depth 갱신
    node 마다 수행 -> BFS 횟수 != 깊이  
    """

    # Solution1 - using bfs
    def maxDepth1(self, root: Optional[TreeNode]) -> int:

        queue = deque([root])
        depth = 0

        while queue:
            depth += 1
            for _ in range(len(queue)):
                cur_node = queue.popleft()
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
        return depth

    """
    depth 마다 수행 -> queue 길이 == depth의 node 수 -> depth가 일정
    -> Solution0와 달리 변수 추가 없어도 됨 & 초기 None 제외 안해도 됨
    depth 마다 수행 -> BFS 횟수 == 깊이 
    """
