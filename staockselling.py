#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(prices):
        profit = 0
        current_amount = prices[0]
        for i in range(1,len(prices)):
            if current_amount < prices[i]:
                profit = max(profit,prices[i]-current_amount)
            
            else:
                current_amount = prices[i]
        return profit


s = Solution
print(s.maxProfit([7,6,4,3,1]))