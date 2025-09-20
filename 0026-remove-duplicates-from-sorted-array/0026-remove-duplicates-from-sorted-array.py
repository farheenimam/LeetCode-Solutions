class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums1 = []
        flag = False
        k = 0
        for i in range (len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    flag = True
                    break
            if flag == False:
                nums1.append(nums[i])
                k= k+1
            else:
                flag = False

        nums[:] = nums1
