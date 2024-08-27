'''
    Denisa-Iulia Vaidasigan
    The Connect Four game has two players placing pieces in column. If one of the player places 4 pieces in a row,
    horizontally, vertically or diagonally, that player wins.
    
'''
import pygame
import math
import random
import sys
from assets.button import Button
from assets.won_check import win_check
from game_modes.ai_player import ai_player

pygame.init()
pygame.font.init()
# Adds font #
game_font = pygame.font.Font('assets/prstartk.ttf', 35)
game_resolution = (1400, 900)

WINDOW = pygame.display.set_mode(game_resolution)
pygame.display.set_caption("Connect Four")
game_background = pygame.image.load('assets/background3.png')

# Global variables #
FIRST_PLAYER = 1
SECOND_PLAYER = 0
FIRST_PLAYER_COLOR = "Yellow"
SECOND_PLAYER_COLOR = "Red"
BOARD_ROWS = 6
BOARD_COLUMNS = 7
BOARD_TOP = 140
BOARD_LEFT = 10
BOARD_WIDTH = 1370
BOARD_HEIGHT = 610
CIRCLE_DIAMETER = min(BOARD_WIDTH // BOARD_COLUMNS, BOARD_HEIGHT // BOARD_ROWS)
CIRCLE_RADIUS = CIRCLE_DIAMETER // 2  
move_made = False

def draw_board(board):
    global BOARD_TOP
    original_board_top = BOARD_TOP
    for row in range(BOARD_ROWS):
        original_board_top += 11
        for column in range(BOARD_COLUMNS):
            x = BOARD_LEFT + (column + 0.5) * (BOARD_WIDTH // BOARD_COLUMNS)
            y = original_board_top + (row + 0.9) * (BOARD_HEIGHT // BOARD_ROWS)
            if board[row][column] == SECOND_PLAYER:
                pygame.draw.circle(WINDOW, SECOND_PLAYER_COLOR, (int(x), int(y)), CIRCLE_RADIUS)
            elif board[row][column] == FIRST_PLAYER:
                pygame.draw.circle(WINDOW, FIRST_PLAYER_COLOR, (int(x), int(y)), CIRCLE_RADIUS)
            else:
                pygame.draw.circle(WINDOW, "Black", (int(x), int(y)), CIRCLE_RADIUS)
        
    pygame.display.update()

def get_next_open_row(board, column):
    global BOARD_ROWS
    for row in range(BOARD_ROWS - 1, -1, -1):
	    if board[row][column] is None:
		    return row
        
# Menu screen #
def menu_screen():
    global game_background
    WINDOW.fill("black")


    while True:
        WINDOW.blit(game_background, (0, 0))
        # Gets mouse position, and renders introduction text #
        MOUSE_POSITION = pygame.mouse.get_pos()
        INTRO_TEXT = game_font.render("Welcome to Connect Four!", True, "White")
        WINDOW.blit(INTRO_TEXT, (310, 300))

        # Creates buttons for all possible game modes: human player and AI player #
        # Buttons change color when hovered over #
        HUMAN_PLAYER = Button(image=None, pos=(700, 450), 
                            text_input="Human Player", font=game_font, base_color="White", hovering_color="Green")
        HUMAN_PLAYER.changeColor(MOUSE_POSITION)
        HUMAN_PLAYER.update(WINDOW)

        AI_PLAYER = Button(image=None, pos=(700, 550), 
                            text_input="AI Player", font=game_font, base_color="White", hovering_color="Green")
        AI_PLAYER.changeColor(MOUSE_POSITION)
        AI_PLAYER.update(WINDOW)
        
        QUIT_BUTTON = Button(image=None, pos=(700, 650), 
                            text_input="Quit", font=game_font, base_color="White", hovering_color="Green")
        
        QUIT_BUTTON.changeColor(MOUSE_POSITION)
        QUIT_BUTTON.update(WINDOW)

        # Checks if the window X or the Quit button are pressed #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if QUIT_BUTTON.checkForInput(MOUSE_POSITION):
                    pygame.quit()
                elif HUMAN_PLAYER.checkForInput(MOUSE_POSITION):
                    play_screen("human")
                else:
                    play_screen("ai")

        pygame.display.update()

# Screen when someone wins #
def won_screen(PLAYER_WON, board):
    while True:
        WINDOW.fill("black")
        WINDOW.blit(game_background, (0, 0))
        draw_board(board)

        # Checks which player won. #
        if PLAYER_WON == 1:
            won_text = game_font.render("FIRST PLAYER WON!", True, "White")
        elif PLAYER_WON == 0:
            won_text = game_font.render("SECOND PLAYER WON!", True, "White")
        else:
            won_text = game_font.render("DRAW!", True, "White")
        SECOND_TEXT = game_font.render("Press R to return to main menu.", True, "White")
        THIRD_TEXT = game_font.render("Press Q to exit.", True, "White")
        WINDOW.blit(won_text, (120, 50))
        WINDOW.blit(SECOND_TEXT, (120, 100))
        WINDOW.blit(THIRD_TEXT, (120, 150))

        pygame.display.update()

        # Checks for events. #
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        menu_screen()
                    if event.key == pygame.K_q:
                        pygame.quit()

# Screen with board #
def play_screen(enemy_type):
    if enemy_type == "human":
        round = random.choice([FIRST_PLAYER, SECOND_PLAYER])

    board = [[None] * BOARD_COLUMNS for _ in range(BOARD_ROWS)]

    while True:
        WINDOW.fill("black")
        
        KEY_TEXT = game_font.render("R - Return, Q - Quit", True, "White")
        WINDOW.blit(KEY_TEXT, (300, 50))

        # Sets circle size #
        pygame.draw.rect(WINDOW, "White", pygame.Rect(10, 140, 1380, 750))

        # Draws circles for table #
        draw_board(board)

        # Checks for events #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    menu_screen()
                if event.key == pygame.K_q:
                    pygame.quit()

            # Handles when player puts piece down #
            if event.type == pygame.MOUSEBUTTONDOWN:
                if enemy_type == "human":                     # Human Player
                    position_x = event.pos[0]
                    column = int(math.floor((position_x/BOARD_WIDTH) * 7))
                    for row in range(BOARD_ROWS - 1, -1, -1):
                        if board[row][column] is None:
                            board[row][column] = round
                            break
                    
                    round += 1
                    round %= 2

                elif enemy_type == "ai":
                    # First player, then AI #
                    position_x = event.pos[0]
                    column = int(math.floor((position_x/BOARD_WIDTH) * 7))
                    row = get_next_open_row(board, column)
                    if row is not None:
                        board[row][column] = FIRST_PLAYER
                        move_made = True

                    
                    draw_board(board)
                    if move_made:
                        column, score = ai_player(board)
                        for row in range(BOARD_ROWS - 1, -1, -1):
                            if board[row][column] is None:
                                board[row][column] = SECOND_PLAYER
                                break
                        move_made = False


        # Winner Check#
        FIRST_PLAYER_WON = win_check(board, FIRST_PLAYER)
        if FIRST_PLAYER_WON is True:
            won_screen(FIRST_PLAYER, board)

        SECOND_PLAYER_WON = win_check(board, SECOND_PLAYER)
        if SECOND_PLAYER_WON is True:
            won_screen(SECOND_PLAYER, board)

        if FIRST_PLAYER_WON is False or SECOND_PLAYER_WON is False:
            won_screen(2)

        pygame.display.update()

menu_screen()