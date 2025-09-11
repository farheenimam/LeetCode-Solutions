class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        for i in range (len(s)-1, -1, -1):
            if s[i] != " ":
                counter += 1
            if counter > 0 and s[i] == " ":
                break
        return counter
        