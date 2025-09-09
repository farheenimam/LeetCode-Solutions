class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        count = 0
        citations = sorted(citations, reverse=True)
        for i in range (0, len(citations)):
            if citations[i] >= i+1:
                count += 1
        
        return count
