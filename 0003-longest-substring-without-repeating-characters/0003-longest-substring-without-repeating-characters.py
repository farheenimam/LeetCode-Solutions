class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        dist = 0
        char_count = {}
        for j in range(len(s)):
            currentChar = s[j]
            if currentChar in char_count:
                i = max(i, char_count[currentChar]+1)
            char_count[currentChar] = j
            dist = max(dist,j-i+1)

        return dist