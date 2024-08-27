# Connect Four Game

## Description
This is a Python implementation of the classic Connect Four game, featuring both a player-vs-player mode and a player-vs-AI mode. The game uses Pygame for its graphical interface and implements a minimax algorithm with alpha-beta pruning for the AI player.

## Features
- Player vs Player mode
- Player vs AI mode
- Graphical user interface using Pygame
- AI opponent using minimax algorithm with alpha-beta pruning

## Requirements
- Python 3.x
- Pygame library

## Installation
1. Ensure you have Python 3.x installed on your system.
2. Install Pygame by running:
   ```
   pip install pygame
   ```
3. Clone this repository or download the source code.

## How to Play
1. Run the main game file:
   ```
   python3 connect_four.py
   ```
2. Use the mouse to select a column to drop your piece.
3. In Player vs Player mode, players take turns.
4. In Player vs AI mode, play against the computer AI.

## Game Controls
- Mouse click: Select column to drop piece
- 'R' key: Return to main menu (when game is over)
- 'Q' key: Quit the game

## Project Structure
- `connect_four.py`: Main game file
- `assets/`: Directory containing game assets (images, fonts)
- `game_modes/`: Directory containing AI player implementation
- `ai_player.py`: AI player implementation

## Acknowledgements
This game was created as a project to learn about game development and AI algorithms in Python.
