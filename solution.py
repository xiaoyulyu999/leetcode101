from collections import deque
from typing import Optional, Any


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def dfs(self, root: Optional[TreeNode]) -> list[Any]:
        q = deque([root])
        values = []

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                print(f"Processing node: {node} (type {type(node)})")  # debug line

                if node:
                    values.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    values.append(None)

        return values

    def run(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        r_p = self.dfs(p)
        r_q = self.dfs(q)

        return r_p == r_q
