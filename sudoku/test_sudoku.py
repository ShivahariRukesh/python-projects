from sudoku import Sudoku

BOARD_SIZE = 9   

def test_initial_game_board_is_empty():
    game = Sudoku(BOARD_SIZE)
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            assert game.get_game_board()[row][col] is None
    print("Test 1 Passed: Initial board is empty")

def test_valid_insert():
    game = Sudoku(BOARD_SIZE)
    assert game.insert_value(0, 0, 1) is True
    assert game.get_game_board()[0][0] == 1
    print("Test 2 Passed: Valid insert")

def test_duplicate_in_row():
    game = Sudoku(BOARD_SIZE)
    game.insert_value(1, 0, 2)
    assert game.insert_value(1, BOARD_SIZE - 1, 2) is False
    print("Test 3 Passed: Duplicate in row")

def test_duplicate_in_column():
    game = Sudoku(BOARD_SIZE)
    game.insert_value(0, 2, 3)
    assert game.insert_value(BOARD_SIZE - 1, 2, 3) is False
    print("Test 4 Passed: Duplicate in column")

def test_duplicate_in_subgrid():
    game = Sudoku(BOARD_SIZE)
    game.insert_value(0, 0, 4)
    assert game.insert_value(1, 1, 4) is False
    print("Test 5 Passed: Duplicate in subgrid")

def test_insert_different_values_same_row():
    game = Sudoku(BOARD_SIZE)
    assert game.insert_value(2, 0, 1) is True
    assert game.insert_value(2, 1, 2) is True
    print("Test 6 Passed: Different values in same row")


test_initial_game_board_is_empty()
test_valid_insert()
test_duplicate_in_row()
test_duplicate_in_column()
test_duplicate_in_subgrid()
test_insert_different_values_same_row()
