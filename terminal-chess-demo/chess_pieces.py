from utils import Piece
class Knight(Piece):
    def is_valid_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end

        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)

        
        if not ((row_diff == 2 and col_diff == 1) or
                (row_diff == 1 and col_diff == 2)):
            return False

        
        target = board[end_row][end_col]
        if target is not None and target.color == self.color:
            return False

        return True
    


class Bishop(Piece):
    def is_valid_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end

        
        if abs(end_row - start_row) != abs(end_col - start_col):
            return False

        
        row_step = 1 if end_row > start_row else -1
        col_step = 1 if end_col > start_col else -1

        
        r, c = start_row + row_step, start_col + col_step
        while (r, c) != (end_row, end_col):
            if board[r][c] is not None:
                return False
            r += row_step
            c += col_step

        
        target = board[end_row][end_col]
        if target is not None and target.color == self.color:
            return False

        return True
    


class Rook(Piece):
    def is_valid_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end

        
        if start_row != end_row and start_col != end_col:
            return False

        
        row_step = 0 if start_row == end_row else (1 if end_row > start_row else -1)
        col_step = 0 if start_col == end_col else (1 if end_col > start_col else -1)

        
        r, c = start_row + row_step, start_col + col_step
        while (r, c) != (end_row, end_col):
            if board[r][c] is not None:
                return False
            r += row_step
            c += col_step

        
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
    


class Queen(Piece):
    def is_valid_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end

        row_diff = end_row - start_row
        col_diff = end_col - start_col

        target = board[end_row][end_col]

        
        if target is not None and target.color == self.color:
            return False

        
        if row_diff == 0: 
            step_row, step_col = 0, 1 if col_diff > 0 else -1
        elif col_diff == 0:  
            step_row, step_col = 1 if row_diff > 0 else -1, 0
        elif abs(row_diff) == abs(col_diff):  
            step_row = 1 if row_diff > 0 else -1
            step_col = 1 if col_diff > 0 else -1
        else:
            return False  

        
        curr_row = start_row + step_row
        curr_col = start_col + step_col
        while (curr_row, curr_col) != (end_row, end_col):
            if board[curr_row][curr_col] is not None:
                return False
            curr_row += step_row
            curr_col += step_col

        return True
