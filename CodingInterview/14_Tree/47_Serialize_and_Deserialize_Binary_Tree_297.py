# 47_Serialize_and_Deserialize_Binary_Tree_297
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize0(self, root: TreeNode) -> str:
        result = ""
        queue = collections.deque([root])
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.pop()
                if not node:
                    result += " "
                    continue
                result += str(node.val)
                left, right = node.left, node.right
                queue.appendleft(left)
                queue.appendleft(right)

        return result

    def deserialize0(self, data: str) -> TreeNode:
        if data == " ":
           return None

        a, rest = data[:1], data[1:]
        root = TreeNode(int(a))
        queue = collections.deque([root])
        while queue:
            node = queue.pop()
            left, right, rest = rest[:1], rest[1:2], rest[2:]
            if len(left) != 0:
                node.left = TreeNode(left)
                queue.appendleft(node.left)
            if len(right) != 0:
                node.right = TreeNode(left)
                queue.appendleft(node.right)
        return root

    """
    bfs로 접근 -> 마지막 노드인지 구분 못하여 불필요한 빈칸/빈 노드가 추가가 됨(개선요소) 
    deserialize에서 오답 => 기존 트리처럼 복구 안됨
    """

    def serialize1(self, root: TreeNode) -> str:
        queue = collections.deque([root])
        result = ['#']

        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                result.append(str(node.val))
            else:
                result.append('#')

        return ' '.join(result)

    def deserialize1(self, data: str) -> TreeNode:
        if data == "# #":
            return None

        nodes = data.split()
        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])

        index = 2
        while queue:
            node = queue.popleft()
            if nodes[index] is not "#":
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1

            if nodes[index] is not "#":
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1

        return root
    """
    빈칸 대신 #으로 구분 & 숫자 사이 빈칸 추가 => data를 쪼갤 때 - 까지 쪼개지는 현상 방지
    serialize 시 불필요한 # 들은 큐에 삽입 되지 않아 처리 되지 않음
    """