class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        ans = []
        for i in range(len(nums)):
           if (i > 0 and nums[i] == nums[i-1]):
            continue
           
           j = i + 1
           k = len(nums) - 1
           while ( j < k):
            sum = nums[i] + nums[k]+ nums[j] 
            if (sum < 0):
                j += 1
            elif sum > 0:
                k -= 1
            else:
                ans.append([nums[i], nums[j], nums[k]])
                j += 1
                while (j < k and nums[j] == nums[j-1]):
                    j += 1

        return ans
        