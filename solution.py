from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def run(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        res = deque()

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node.val is not None:
                    level.append(node.val)
                q.append(node.left) if node.left else None
                q.append(node.right) if node.right else None
            if level:
                res.appendleft(level)

        return list(res)
