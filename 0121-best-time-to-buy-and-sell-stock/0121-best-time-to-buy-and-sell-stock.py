class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
    
        profit = 0
        buy = prices[0]
        for num in prices[1:]:
            if (buy > num):
                buy = num
            profit = max(profit, num - buy)
        return profit       
        