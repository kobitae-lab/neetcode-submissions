class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.check_rows(board) and self.check_columns(board) and self.check_grids(board)
        
    def check_rows(self, board):
        d = set()
        for row in board:
            d.clear()
            for value in row:
                if value in d and value != '.':
                    return False
                else:
                    d.add(value)
        return True
    

    def check_columns(self, board):
        d = set()
        i = 0
        while i <= 8:
            d.clear()
            for row in board:
                if row[i] in d and row[i] != '.':
                    return False
                else:
                    d.add(row[i])
            i += 1
        return True
    

    def check_grids(self, board):
        i = 0
        j = 0
        d = set()
        while i <= 8:
            if i == 3 or i == 6:
                d.clear()
            j = 0
            while j <= 2:
                if board[i][j] in d and board[i][j] != '.':
                    return False
                else:
                    d.add(board[i][j])
                    j += 1
            i += 1
        d.clear()
        i = 0
        while i <= 8:
            if i == 3 or i == 6:
                d.clear()
            j = 3
            while j <= 5:
                if board[i][j] in d and board[i][j] != '.':
                    return False
                else:
                    d.add(board[i][j])
                    j += 1
            i += 1
        d.clear()
        i = 0
        while i <= 8:
            if i == 3 or i == 6:
                d.clear()
            j = 6
            while j <= 8:
                if board[i][j] in d and board[i][j] != '.':
                    return False
                else:
                    d.add(board[i][j])
                    j += 1
            i += 1
        return True



