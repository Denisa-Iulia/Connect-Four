from assets.count_scoring import score_position
from assets.won_check import win_check
import math
from copy import deepcopy

BOARD_ROWS = 6
BOARD_COLUMNS = 7
FIRST_PLAYER = 1
SECOND_PLAYER = 0

def get_next_open_row(board, column):
    global BOARD_ROWS
    for row in range(BOARD_ROWS - 1, -1, -1):
	    if board[row][column] is None:
		    return row

def get_valid_locations(board):
    global BOARD_COLUMNS, BOARD_ROWS
    valid_locations = []
    for column in range(BOARD_COLUMNS):
        checked = False
        for row in range(BOARD_ROWS - 1, -1, -1):
            if board[row][column] is None:
                valid_locations.append(column)
                checked = True
            if checked is True:
                break

    return valid_locations

def ai_player(board, depth = 5, maximizing_player = True, alpha = -math.inf, beta = math.inf):
    global BOARD_COLUMNS, FIRST_PLAYER, SECOND_PLAYER   

    # Checks each alternative and gives scoring #
    FIRST_PLAYER_WON = win_check(board, FIRST_PLAYER)
    SECOND_PLAYER_WON = win_check(board, SECOND_PLAYER)

    print(FIRST_PLAYER_WON, SECOND_PLAYER_WON)

    if FIRST_PLAYER_WON is True: # when minimizing player wins
        return (None, -999)
    elif SECOND_PLAYER_WON is True: # when maximizing player wins
        return (None, 999)
    elif FIRST_PLAYER_WON is False or SECOND_PLAYER_WON is False: # when there is a draw
        return (None, 0)
    elif depth == 0:
        return (None, score_position(board, SECOND_PLAYER))
    
    valid_locations = get_valid_locations(board)

    if maximizing_player:
        max_evaluation = -math.inf
        # For each column, checks for available position and places piece #
        for column in valid_locations:
            board_copy = deepcopy(board)
            row = get_next_open_row(board_copy, column)
            board_copy[row][column] = SECOND_PLAYER
            evaluation = ai_player(board_copy, depth - 1, False, alpha, beta)[1]
            alpha = max(max_evaluation, evaluation)
            if max_evaluation < evaluation:
                max_evaluation = evaluation
                best_column = column
            if beta <= alpha:
                break
        return (best_column, max_evaluation)
    

    else:
        min_evaluation = math.inf
        for column in valid_locations:
            board_copy = deepcopy(board)
            row = get_next_open_row(board_copy, column)
            board_copy[row][column] = FIRST_PLAYER
            evaluation = ai_player(board_copy, depth - 1, True, alpha, beta)[1]
            beta = min(min_evaluation, evaluation)
            if min_evaluation > evaluation:
                min_evaluation = evaluation
                best_column = column  
            if beta <= alpha:
                break
        return (best_column, min_evaluation)
