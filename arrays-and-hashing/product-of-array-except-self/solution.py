class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        total = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                total *= num
        if zero_count > 1:
            nums = [0 for num in nums]
        elif zero_count == 1:
            nums = [0 if num != 0 else int(total) for num in nums]
        else:
            nums = [int(total / num) for num in nums]
        return nums
