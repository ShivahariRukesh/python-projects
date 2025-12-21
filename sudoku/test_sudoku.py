from sudoku import Sudoku


def test_initial_game_board_is_empty():
    game = Sudoku()
    for row in range(4):
        for col in range(4):
            assert game.get_game_board()[row][col] is None
    print("Test 1 Passed : The initial game board  is empty")

def test_valid_insert():
    game = Sudoku()
    assert game.insert_value(0, 0, 1) is True
    assert game.get_game_board()[0][0] == 1
    print("Test 2 Passed: The valid insert")



def test_duplicate_in_row():
    game = Sudoku()
    game.insert_value(1, 0, 2)
    assert game.insert_value(1, 3, 2) is False
    print("Test 3 Passed: The duplicate insertion in a row")



def test_duplicate_in_column():
    game = Sudoku()
    game.insert_value(0, 2, 3)
    assert game.insert_value(3, 2, 3) is False
    print("Test 4 Passed: The duplicate insertion in a column")



def test_duplicate_in_subgrid():
    game = Sudoku()
    game.insert_value(0, 0, 4)
    assert game.insert_value(1, 1, 4) is False
    print("Test 5 Passed: The duplicate insertion in the subgrid")



def test_insert_different_values_same_row():
    game = Sudoku()
    assert game.insert_value(2, 0, 1) is True
    assert game.insert_value(2, 1, 2) is True
    print("Test 6 Passed: Different values insertion in a same row")


test_initial_game_board_is_empty()
test_valid_insert()
test_duplicate_in_row()
test_duplicate_in_column()
test_duplicate_in_subgrid()
test_insert_different_values_same_row()