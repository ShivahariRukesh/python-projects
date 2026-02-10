from chess_pieces import Knight,Rook,Bishop,Pawn
from utils import parse_position, print_board


# Initialize board
board = [[None for _ in range(8)] for _ in range(8)]
board[0][0] = Rook('b', 'R')  # Black rook at a8
board[7][7] = Rook('w', 'R')  # White rook at h1


board[0][2] = Bishop('b', 'B')  # Black bishop at c8
board[7][5] = Bishop('w', 'B')  # White bishop at f1


board[0][1] = Knight('b', 'K')  # Black bishop at b8
board[7][6] = Knight('w', 'K')  # White bishop at g1

# Black pawns
for col in range(8):
    board[1][col] = Pawn('b', 'P')

# White pawns
for col in range(8):
    board[6][col] = Pawn('w', 'P')
    
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
