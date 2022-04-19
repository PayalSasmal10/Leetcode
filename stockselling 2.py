# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices) -> int:
        current_value= prices[0]
        profit = 0
        for i in range(len(prices)):
            if current_value < prices[i]:
                profit += prices[i]-current_value
                current_value = prices[i]
                
        return profit
        
s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))