class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        r, c = 0, 0
        dr, dc = 0, 1 
        len_of_r = len(matrix)
        len_of_c = len(matrix[0])
        spiral = []
       
        for i in range(len_of_r * len_of_c):
            spiral.append(matrix[r][c])
            matrix[r][c] = "."

            if not 0 <= r + dr < len_of_r or not 0 <= c + dc < len_of_c or matrix[r+dr][c+dc] == ".":
                dc, dr = -dr, dc
            r += dr
            c += dc
        return spiral
