from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def min_swaps_to_sort(self, arr: List[int]) -> int:
        sorted_arr = sorted(arr)
        # [1, 2, 3, 4, 5, 6, 7]
        hash_ = {value: id for id, value in enumerate(arr)}
        # {1: 0, 3: 1, 2: 2, 7: 3, 6: 4, 5: 5, 4: 6}
        # hash_ uses to identify the place where the element in sorted arr is in the un-sorted array
        # so that, can be swap in the old array.
        swaps = 0

        for i in range(len(arr)):
            if arr[i] != sorted_arr[i]:
                swaps += 1

                # tracking arr[i]
                j = hash_[sorted_arr[i]]
                arr[i], arr[j] = arr[j], arr[i]

                #update the hash_, so that at then end the hash_ should have the same value to index as a sorted array.
                hash_[arr[j]] = j
                hash_[arr[i]] = i
        return swaps

    def run(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        queue = deque([root])
        total_swaps = 0

        while queue:
            level_size = len(queue)
            level_values = []

            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            total_swaps += self.min_swaps_to_sort(level_values)

        return total_swaps
