import numpy
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [1] * len(nums)
        left = 1
        for i in range(0, len(nums)):
            answer[i] *= left
            left *= nums[i]
        right = 1    
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= right
            right *= nums[i] 
        return answer         
        