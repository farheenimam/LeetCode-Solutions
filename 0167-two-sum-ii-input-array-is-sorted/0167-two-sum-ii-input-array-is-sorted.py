class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum = 0
        a = 0
        b = len(numbers) - 1

        while ( a < b):
            sum = numbers[a] + numbers[b]
            if (sum == target):
                return [a+1, b+1]
            elif (sum < target):
                a+= 1
            else:
                b-=1

        return indexes      
        