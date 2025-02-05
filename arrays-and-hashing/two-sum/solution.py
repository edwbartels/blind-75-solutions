class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}
        for index, num in enumerate(nums):
            if (target - num) in num_map:
                return [num_map[target - num], index]
            num_map[num] = index
