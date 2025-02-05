class Solution:
    def findMin(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if nums[0] < nums[-1]:
            return nums[0]

        l = 0
        r = len(nums) - 1

        while l <= r:
            if r - l <= 1:
                return min(nums[l], nums[r])

            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid

            else:
                r = mid
