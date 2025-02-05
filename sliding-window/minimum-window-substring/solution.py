from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_map = Counter(t)
        result = ""
        left = 0
        missing = len(t)

        for right in range(len(s)):
            if s[right] in char_map:
                if char_map[s[right]] > 0:
                    missing -= 1
                char_map[s[right]] -= 1

            while missing == 0:
                if result == "" or (right - left + 1) < len(result):
                    result = s[left : right + 1]

                if s[left] in char_map:
                    char_map[s[left]] += 1
                    if char_map[s[left]] > 0:
                        missing += 1
                left += 1

        return result
