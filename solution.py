from collections import deque
from typing import Optional, Any


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    '''
    Use DFS for each level. If every level is palindrome, return True.
    '''

    def dfs(self, root: Optional[TreeNode]) -> list[Any]:
        if not root:
            return []

        q = deque([root])
        bool_list = []
        while q:
            values = []
            for _ in range(len(q)):
                node = q.popleft()
                values.append(node.val)
                q.append(node.left) if node.left else None
                q.append(node.right) if node.right else None
            if len(values) == 1:
                bool_list.append(True)
            else:
                half = len(values) // 2
                for i in range(half):
                    if values[i] != values[-i - 1]:
                        bool_list.append(False)
                    else:
                        bool_list.append(True)
        return bool_list

    def run(self, root: Optional[TreeNode]) -> bool:
        return all(self.dfs(root))
