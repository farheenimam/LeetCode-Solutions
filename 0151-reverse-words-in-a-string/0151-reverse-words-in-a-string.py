class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        cleaned_strings = s.split()
        reverse_string = " ".join(cleaned_strings[::-1])
        return reverse_string
        