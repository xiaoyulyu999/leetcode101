from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def run(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([(root, 0)])  # (node, depth)

        while q:
            for _ in range(len(q)):
                node, depth = q.popleft()
                # Check if it's a leaf node
                if not node.left and not node.right:
                    print(node.val, depth)
                    return depth + 1
                if node.left:
                    q.append((node.left, depth + 1))
                if node.right:
                    q.append((node.right, depth + 1))
        return 0
