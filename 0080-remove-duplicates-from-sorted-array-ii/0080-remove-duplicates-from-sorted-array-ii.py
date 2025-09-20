class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)

        num1= []
        temp = None
        k = 0
        count = 0
        for i in range (0, len(nums)):
            if (temp == nums[i] and count < 1):
                num1.append(nums[i])
                count = count + 1
                k = k + 1
            elif (temp != nums[i]):
                num1.append(nums[i])
                print(nums[i])
                count = 0
            temp = nums[i]

        nums[:] = num1
                      