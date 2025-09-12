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
        print(seq) 
        index , d = numRows - 1, 1
        s = s[numRows: len(s)]
        print(s)
        for char in s:
            if index == 0:
                d = 1
            elif index == numRows - 1:
                d = -1
            index += d
            seq[index]+= char
        print(seq)
        # for i in range(numRows):
        #     seq[i] = ''.join(seq[i])

        return ''.join(seq)    
        