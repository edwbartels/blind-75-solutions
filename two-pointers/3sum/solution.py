class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            num = nums[i]
            front = i + 1
            back = len(nums) - 1

            while front < back:
                sum = num + nums[front] + nums[back]

                if sum < 0:
                    front += 1
                elif sum > 0:
                    back -= 1
                else:
                    result.append([num, nums[front], nums[back]])
                    front += 1
                    back -= 1
                    while front < back and nums[front] == nums[front - 1]:
                        front += 1
                    while front < back and nums[back] == nums[back + 1]:
                        back -= 1

        return result
