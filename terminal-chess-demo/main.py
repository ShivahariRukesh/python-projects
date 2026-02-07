class Piece:
    def __init__(self, color, name):
        self.color = color  # 'w' or 'b'
        self.name = name    # 'P', 'R', 'N', 'B', 'Q', 'K'

    def is_valid_move(self, start, end, board):
        return False

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



def print_board(board):
    print("\ta \tb \tc \td \te \tf \tg \th")
    for row_idx, row in enumerate(board):
        print(8 - row_idx, end=" ")
        for square in row:
            if square is None:
                print("\t.", end=" ")
            else:
                print("\t"+square.color + square.name, end=" ")
        print()
    print()


def parse_position(notation):
    col_map = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
    row_map = {'8':0, '7':1, '6':2, '5':3, '4':4, '3':5, '2':6, '1':7}

    col = col_map[notation[0]]
    row = row_map[notation[1]]
    return (row, col)


# Initialize board
board = [[None for _ in range(8)] for _ in range(8)]
board[0][0] = Rook('b', 'R')  # Black rook at a8
board[7][7] = Rook('w', 'R')  # White rook at h1


board[0][2] = Bishop('b', 'B')  # Black bishop at c8
board[7][5] = Bishop('w', 'B')  # White bishop at f1


board[0][1] = Knight('b', 'K')  # Black bishop at b8
board[7][6] = Knight('w', 'K')  # White bishop at g1


turn = 'w'

while True:
    print_board(board)
    move = input(f"{turn}'s move (e.g., e2 e4): ")

    try:
        start_str, end_str = move.split()
        start_pos = parse_position(start_str)
        end_pos = parse_position(end_str)
    except:
        print("Invalid input format.")
        continue

    piece = board[start_pos[0]][start_pos[1]]

    if piece and piece.color == turn:
        if piece.is_valid_move(start_pos, end_pos, board):
            board[end_pos[0]][end_pos[1]] = piece
            board[start_pos[0]][start_pos[1]] = None
            turn = 'b' if turn == 'w' else 'w'
        else:
            print("Invalid move for that piece.")
    else:
        print("No piece there or not your turn!")
