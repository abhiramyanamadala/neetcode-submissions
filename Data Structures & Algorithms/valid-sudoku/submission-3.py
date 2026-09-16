class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows
        for i in range(9):
            hash_set = set()

            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in hash_set:
                        return False

                    hash_set.add(board[i][j])

        # Check columns
        for i in range(9):
            hash_set = set()

            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in hash_set:
                        return False

                    hash_set.add(board[j][i])

        # Check 3x3 boxes
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):

                hash_set = set()

                for i in range(row, row + 3):
                    for j in range(col, col + 3):

                        if board[i][j] != ".":
                            if board[i][j] in hash_set:
                                return False

                            hash_set.add(board[i][j])

        return True