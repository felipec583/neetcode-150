from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_lookup = {}
        for i, num in enumerate(nums):
            needed = target - num
            if num in pair_lookup:
                return [pair_lookup[num], i]
            else:
                pair_lookup[needed] = i
