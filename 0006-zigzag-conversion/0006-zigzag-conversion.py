class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        if numRows == 1 or numRows >= len(s):
            return s

        seq = [s[i] for i in range(numRows)]   
  
        index , d = numRows - 1, 1
        s = s[numRows: len(s)]
    
        for char in s:
            if index == 0:
                d = 1
            elif index == numRows - 1:
                d = -1
            index += d
            seq[index]+= char
        print(seq)

        return ''.join(seq)    
        