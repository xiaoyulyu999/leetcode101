from typing import List


class Solution:

    def run(self, nums: List[int], target: int) -> List[int]:

        hashtable = {}
        for idx, num in enumerate(nums):

            if target - num in hashtable:
                return [hashtable[target - num], idx]
            else:
                hashtable[num] = idx
        return []
