from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        str_map = defaultdict(list)

        for string in strs:
            char_count = [0] * 26

            for char in string:
                char_count[ord(char) - ord("a")] += 1

            key = tuple(char_count)
            str_map[key].append(string)

        return list(str_map.values())
