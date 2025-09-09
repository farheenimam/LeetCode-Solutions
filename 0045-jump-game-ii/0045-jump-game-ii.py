class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = f = jump = 0
        while(f < len(nums)-1):
            farthest = 0
            for i in range(n, f+1):
                farthest = max(farthest,i+nums[i])
            near = f
            f= farthest
            jump += 1

        return jump