from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sum_node(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return root.val + self.sum_node(root.left) + self.sum_node(root.right)

    def run(self, root: Optional[TreeNode]) -> int:
        return 1
