class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0 # At the starting point
        right = len(height) - 1 # placed at the end of the array
        max_space = 0
        while (left< right):
            space = min(height[left], height[right]) * (right - left)
            max_space = max(max_space, space)
            if (height[left] < height[right]):
                left += 1
            else:
                right -= 1

        return max_space       