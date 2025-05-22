from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def run(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        values = []
        max_ = 0
        while q:
            level_length = len(q)

            for _ in range(level_length):
                node = q.popleft()
                max_ = node.val if node.val > max_ else max_
                if node:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            values.append(max_)
        return values
