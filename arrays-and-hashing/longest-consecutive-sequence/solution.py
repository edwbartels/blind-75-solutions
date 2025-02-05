class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        next_map = {}
        max_length = 0

        for num in nums:
            count = 1
            current = num

            if num not in next_map:
                next_map[num] = {"prev": False, "next": False}

            if (num - 1) in next_map:
                next_map[num]["prev"] = True
                next_map[num - 1]["next"] = True

            if (num + 1) in next_map:
                next_map[num]["next"] = True
                next_map[num + 1]["prev"] = True

            while current in next_map and next_map[current]["prev"]:
                count += 1
                current -= 1

            current = num

            while current in next_map and next_map[current]["next"]:
                count += 1
                current += 1

            if count > max_length:
                max_length = count

        return max_length
