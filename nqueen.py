# This function is used to display the chess board
def display_board(board):
    print("----------Board State----------")
    for i in board:
        print(i)
    print("")


# these is used to check if the diagonal is safe or not
def is_left_diagonal_safe(board, row, column):
    # checking if row < 0, then returning 1
    if (row <= 0 or column <= 0):
        return 1

    width = row
    for i in range(0, width):
        row -= 1
        column -= 1

        if (board[row][column]):
            return 0

    return 1


# these is used to check if the diagonal is safe or not
def is_right_diagonal_safe(board, row, column):
    # checking if row < 0, then returning 1
    if (row <= 0 or column <= 0):
        return 1

    width = row
    for i in range(0, width):
        row -= 1
        column += 1

        # if condition if the values are out of bound
        if (column >= width):
            return 1

        print(row, column)
        if (board[row][column]):
            return 0

    return 1


def is_column_safe(board, row, column):
    # checking if row < 0, then returning 0
    if (row < 0):
        return 1

    for i in range(0, row):
        if (board[i][column] == 1):
            return 0

    return 1


def is_safe(board, row, column):
    c1 = is_column_safe(board, row, column)
    c2 = is_left_diagonal_safe(board, row, column)
    c3 = is_right_diagonal_safe(board, row, column)

    if c1 and c2 and c3:
        return True
    else:
        return False


def chess_solve(board, row, num):
    # Check if we have placed all queens on the board and display the result.
    if row >= num:
        display_board(board)
        return True

    # Try placing a queen on each column of the current row.
    for col in range(num):
        safe = is_safe(board, row, col)
        # Check if it's safe to place a queen at this position.
        if safe:
            # Place the queen at this position and move to the next row.
            board[row][col] = 1
            print(f"Queen placed at row {row + 1}, column {col + 1}")

            display_board(board)
            # Recursively call the function to place queens on the next row.
            if chess_solve(board, row + 1, num):
                return True

            # If we cannot place a queen on the next row, backtrack and remove the queen from this position.
            board[row][col] = 0

    # If we cannot place any queen on this row, return False.
    return False


if __name__ == "__main__":
    num = 4
    board_matrix = []
    for i in range(num):
        board_matrix.append([0] * num)

    print("Initial State")
    display_board(board_matrix)

    chess_solve(board_matrix, 0, num)