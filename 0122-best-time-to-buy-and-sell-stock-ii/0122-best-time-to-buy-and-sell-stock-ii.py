class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        profit = 0
        temp1 = 0 
        for num in prices[1:]:
            if (profit > 0):
                if (num <= temp1):
                    buy = num
                if (temp1 < num):
                    buy = temp1

            if (profit == 0):         
                if buy > num:
                    buy = num
            profit = profit + (num - buy)
            temp1 = num    
            

        return profit    