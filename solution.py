from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def bfs_bool(self, current_sum: int, root: Optional[TreeNode], targetSum) -> bool:
        if not root:
            return False
        current_sum += root.val
        if not root.left and not root.right:
            return current_sum == targetSum
        else:
            return (self.bfs_bool(current_sum + root.val, root.left, targetSum)
                    or
                    self.bfs_bool(current_sum + root.val, root.right, targetSum))


    def run(self, root: Optional[TreeNode], targetSum: int) -> bool:

        return self.bfs_bool(0, root, targetSum)
