class Piece:
    def __init__(self, color, name):
        self.color = color  # 'w' or 'b'
        self.name = name    # 'P', 'R', 'N', 'B', 'Q', 'K'

    def is_valid_move(self, start, end, board):
        return False
    



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