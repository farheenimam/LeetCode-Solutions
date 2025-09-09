class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # no. of candies equal to the number of rating
        candies = [1] * len(ratings)
        candy = 0
        print(candies)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] += candies[i-1]

        
        for i in range(len(ratings) - 1, 0, -1):
            if (ratings[i-1] > ratings[i]):
                candies[i-1] = max(candies[i] + 1, candies[i-1]) 
            candy += candies[i-1]    
        return candy + candies[len(ratings)-1] 
        