from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]):
        diff = [0] * (len(nums) + 1)

        for query in queries:
            inc, dec = query

            diff[inc] += 1
            diff[dec + 1] -= 1

        for i in range(1, len(diff)):
            diff[i] += diff[i - 1]

        return all(diff[x] >= nums[x] for x in range(len(nums)))