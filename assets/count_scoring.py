FIRST_PLAYER = 1
SECOND_PLAYER = 0
BOARD_ROWS = 6
BOARD_COLUMNS = 7
WINDOW_LENGTH = 4

def evaluate_window(window, piece):
	global FIRST_PLAYER, SECOND_PLAYER
	score = 0
	if piece == FIRST_PLAYER:
		opponent_piece = SECOND_PLAYER
	else:
		opponent_piece = FIRST_PLAYER

	if window.count(piece) == 3 and window.count(None) == 1:
		score += 100
	elif window.count(piece) == 2 and window.count(None) == 2:
		score += 50

	if window.count(opponent_piece) == 3 and window.count(None) == 1:
		score -= 300

	return score

def score_position(board, piece):
	global BOARD_COLUMNS, BOARD_ROWS, WINDOW_LENGTH
	score = 0

	## Score center column
	center_list = [int(row[BOARD_COLUMNS//2]) for row in board if row[BOARD_COLUMNS//2] is not None]
	center_count = center_list.count(piece)
	score += center_count * 3

	## Score Horizontal
	for r in range(BOARD_ROWS):
		row_list = [int(i) if i is not None else None for i in board[r]]
		for c in range(BOARD_COLUMNS - 3):
			window = row_list[c:c+WINDOW_LENGTH]
			score += evaluate_window(window, piece)

	## Score Vertical
	for c in range(BOARD_COLUMNS):
		column_list = [int(board[r][c]) if board[r][c] is not None else None for r in range(BOARD_ROWS)]
		for r in range(BOARD_ROWS - 3):
			window = column_list[r:r+WINDOW_LENGTH]
			score += evaluate_window(window, piece)

	## Score posiive sloped diagonal
	for r in range(BOARD_ROWS - 3):
		for c in range(BOARD_COLUMNS - 3):
			window = [int(board[r+i][c+i]) if board[r+i][c+i] is not None else None for i in range(WINDOW_LENGTH)]
			score += evaluate_window(window, piece)

# Score negative sloped diagonal
	for r in range(BOARD_ROWS - 3):
		for c in range(BOARD_COLUMNS - 3):
			window = [int(board[r+3-i][c+i]) if board[r+3-i][c+i] is not None else None for i in range(WINDOW_LENGTH)]
			score += evaluate_window(window, piece)

	return score