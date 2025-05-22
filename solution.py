from collections import deque
from typing import Optional, List


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
        leaf_list = []
        queue = deque([root])

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    if node.val is not None:
                        level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                leaf_list.append(level)

        return leaf_list
