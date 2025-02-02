class Solution(object):
    def isValidSudoku(self, board):
        r = defaultdict(set)
        c = defaultdict(set)
        b = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board)):

                if (board[row][col] == "."):
                    continue 
                
                if (board[row][col] in r[row] or board[row][col] in c[col] or board[row][col] in b[row // 3, col // 3]):
                    return False
                
                r[row].add(board[row][col])
                c[col].add(board[row][col])
                b[(row // 3, col // 3)].add(board[row][col])

        return True
        