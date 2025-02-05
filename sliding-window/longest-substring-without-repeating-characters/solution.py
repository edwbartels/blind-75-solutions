class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = set()
        max_count = 0
        left = 0

        for right in range(len(s)):
            while s[right] in char_map:
                char_map.remove(s[left])
                left += 1
            char_map.add(s[right])
            max_count = max(max_count, right - left + 1)

        return max_count
