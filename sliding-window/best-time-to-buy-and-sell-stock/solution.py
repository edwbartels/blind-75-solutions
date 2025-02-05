class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
                right = left + 1
            else:
                max_profit = max(max_profit, prices[right] - prices[left])
                right += 1

        return max_profit
