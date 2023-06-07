# defining MAX AND MIN 
MAX = 1000
MIN = -1000

# defining X and O 
ai_mark = "X"
human_mark = "O"

# This function checks if the player with the given marker has won the game.
# It returns True if the player has won, and False otherwise.
def check_if_won(board, cur_marker): 
    if (board[0] == cur_marker and board[1] == cur_marker and board[2] == cur_marker) or \
       (board[3] == cur_marker and board[4] == cur_marker and board[5] == cur_marker) or \
       (board[6] == cur_marker and board[7] == cur_marker and board[8] == cur_marker) or \
       (board[0] == cur_marker and board[3] == cur_marker and board[6] == cur_marker) or \
       (board[1] == cur_marker and board[4] == cur_marker and board[7] == cur_marker) or \
       (board[2] == cur_marker and board[5] == cur_marker and board[8] == cur_marker) or \
       (board[0] == cur_marker and board[4] == cur_marker and board[8] == cur_marker) or \
       (board[2] == cur_marker and board[4] == cur_marker and board[6] == cur_marker): 
        return True 
    else: 
        return False

# This function creates a new empty Tic-Tac-Toe board.
# It returns a list representing the board, with each element initially set to its index.
def create_board(): 
    return list(range(9))

# This function returns a list of the indices of all the empty cells on the board.
# An empty cell is one that does not contain either the AI or human marker.
def get_empty_cells_of_boards(board): 
    return [i for i in range(9) if board[i] not in (ai_mark, human_mark)]

# This function implements the minimax algorithm to find the best move for the AI.
# It returns a dictionary containing the index of the best move and its associated score.
# The depth parameter is used to weight the score based on how many moves were made to reach that state.
# The alpha and beta parameters are used for alpha-beta pruning, which helps to reduce the search space.
# The is_maximizing_player parameter is a boolean that is True when it's the AI's turn to play, and False otherwise.
def minimax(board, depth, alpha, beta, is_maximizing_player):
    # storing all the empty cells from the board 
    empty_cells = get_empty_cells_of_boards(board)

    # checking if there is a terminal state 
    if check_if_won(board, human_mark): 
        return {'score': -10 + depth}
    elif check_if_won(board, ai_mark): 
        return {'score': 10 - depth} 
    elif len(empty_cells) == 0:  
        return {'score': 0}

    # maximizing player's turn
    if is_maximizing_player:
        best_score = {'index': None, 'score': MIN}
        for i in empty_cells:
            curr_play = {}
            curr_play['index'] = i
            board[i] = ai_mark

            # recursive call to minimax with updated board and depth
            result = minimax(board, depth + 1, alpha, beta, False)
            curr_play['score'] = result['score']
            
            board[i] = curr_play['index']

            if curr_play['score'] > best_score['score']:
                best_score = curr_play

            alpha = max(alpha, best_score['score'])
            
            if beta <= alpha:
                break

        return best_score

    # minimizing player's turn
    else:
        best_score = {'index': None, 'score': MAX}
        for i in empty_cells:
            curr_play = {}
            curr_play['index'] = i
            board[i] = human_mark

            result = minimax(board, depth + 1, alpha, beta, True)
            curr_play['score'] = result['score']
            
            board[i] = curr_play['index']

            if curr_play['score'] < best_score['score']:
                best_score = curr_play
            
            beta = min(beta, best_score['score'])
            
            if beta <= alpha:
                break

        return best_score

def print_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("-" * 9)
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("-" * 9)
    print(f"{board[6]} | {board[7]} | {board[8]}")

def play_game():
    board = create_board()
    print_board(board)
    
    while True:
        # human turn
        human_choice = int(input("Enter cell number to put O (1-9): "))
        if board[human_choice-1] in (ai_mark, human_mark):
            print("Cell already occupied!")
            continue
        board[human_choice-1] = human_mark
        print_board(board)

        # check if human wins
        if check_if_won(board, human_mark):
            print("You won!")
            break

        # check for tie game
        if len(get_empty_cells_of_boards(board)) == 0:
            print("Tie game!")
            break

        # AI turn
        ai_choice = minimax(board, 0, MIN, MAX, True)['index']
        board[ai_choice] = ai_mark
        print(f"AI chose cell {ai_choice+1}")
        print_board(board)

        # check if AI wins
        if check_if_won(board, ai_mark):
            print("AI won!")
            break

if __name__ == "__main__":
    play_game()