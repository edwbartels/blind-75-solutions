class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        max_freq = 0
        max_count = 0
        left = 0

        for right in range(len(s)):
            freq_map[s[right]] = freq_map.get(s[right], 0) + 1

            max_freq = max(max_freq, freq_map[s[right]])

            if (right - left + 1) - max_freq > k:
                freq_map[s[left]] -= 1
                left += 1

            max_count = max(max_count, right - left + 1)

        return max_count
