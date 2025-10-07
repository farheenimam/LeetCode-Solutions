class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Declaring 3 hash sets
        rows = defaultdict(set)
        col = defaultdict(set)
        sub_box = defaultdict(set)
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if board[r][c] == '.':
                    continue
                if (num in rows[r] or num in col[c] or num in sub_box[(r// 3, c// 3)]):
                    return False
                # If not present add them to the hash set
                rows[r].add(num)
                col[c].add(num)
                sub_box[(r//3, c//3)].add(num)

        return True
                