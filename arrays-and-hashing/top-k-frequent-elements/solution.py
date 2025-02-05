from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq_map = Counter(nums)
        max_freq = max(freq_map.values())
        bucket = [[] for _ in range(max_freq + 1)]

        for num, freq in freq_map.items():
            bucket[freq].append(num)

        result = []
        count = -1
        while len(result) < k:
            result.extend(bucket[count])
            count -= 1
        return result
