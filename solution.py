from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]):
        for query in queries:
            inc, dec = query
            diff = [0] * (len(nums) + 1)

            nums[inc] += 1
            nums[dec + 1] -= 1
