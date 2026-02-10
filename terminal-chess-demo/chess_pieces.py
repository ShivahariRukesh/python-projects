from utils import Piece
class Knight(Piece):
    def is_valid_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end

        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)

        # Knight moves in an L shape
        if not ((row_diff == 2 and col_diff == 1) or
                (row_diff == 1 and col_diff == 2)):
            return False

        # Destination square
        target = board[end_row][end_col]
        if target is not None and target.color == self.color:
            return False

        return True
    


class Bishop(Piece):
    def is_valid_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end

        # Must move diagonally
        if abs(end_row - start_row) != abs(end_col - start_col):
            return False

        # Determine direction
        row_step = 1 if end_row > start_row else -1
        col_step = 1 if end_col > start_col else -1

        # Check path blocking (exclude destination square)
        r, c = start_row + row_step, start_col + col_step
        while (r, c) != (end_row, end_col):
            if board[r][c] is not None:
                return False
            r += row_step
            c += col_step

        # Destination square
        target = board[end_row][end_col]
        if target is not None and target.color == self.color:
            return False

        return True
    


class Rook(Piece):
    def is_valid_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end

        # Must move in a straight line
        if start_row != end_row and start_col != end_col:
            return False

        # Determine direction
        row_step = 0 if start_row == end_row else (1 if end_row > start_row else -1)
        col_step = 0 if start_col == end_col else (1 if end_col > start_col else -1)

        # Check path blocking (exclude destination square)
        r, c = start_row + row_step, start_col + col_step
        while (r, c) != (end_row, end_col):
            if board[r][c] is not None:
                return False
            r += row_step
            c += col_step

        # Destination square
        target = board[end_row][end_col]
        if target is not None and target.color == self.color:
            return False

        return True
    



class Pawn(Piece):
    def is_valid_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end

        direction = -1 if self.color == 'w' else 1
        start_row_home = 6 if self.color == 'w' else 1

        row_diff = end_row - start_row
        col_diff = abs(end_col - start_col)

        target = board[end_row][end_col]

        if col_diff == 0 and row_diff == direction:
            if target is None:
                return True

        if col_diff == 0 and row_diff == 2 * direction and start_row == start_row_home:
            intermediate_row = start_row + direction
            if board[intermediate_row][start_col] is None and target is None:
                return True

        if col_diff == 1 and row_diff == direction:
            if target is not None and target.color != self.color:
                return True

        return False