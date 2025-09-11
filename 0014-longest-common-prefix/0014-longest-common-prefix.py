class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = []

        if len(strs) > 0 and strs:
            sorted_str = sorted(strs)
            first, last = sorted_str[0], sorted_str[-1]
            for i in range(len(first)):
                if len(last) > i and last[i] == first[i]:
                    prefix.append(first[i])
                else:
                    return "".join(prefix)

        return "".join(prefix)