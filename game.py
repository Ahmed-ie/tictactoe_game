from cs1lib import *

# Here we are defining some constants for our Tic-Tac-Toe game.
# BOARD_SIZE is the size of the board (3x3),
# CELL_SIZE is the size of each cell in pixels,
# and WIDTH and HEIGHT are the dimensions of the game window.
# Constants for the game
BOARD_SZ = 3
CELL_SIZE = 100
WIDTH = HEIGHT = CELL_SIZE * BOARD_SZ

# These are our game state variables.
# game_started checks if the game has begun,
# winner will store the winner of the game, if there is one.
game_started = False
winner = None

# Initialize the game board as a 3x3 grid of empty strings.
board = []
for row in range(BOARD_SZ):
    # Create an empty row
    board_row = []

    for col in range(BOARD_SZ):
        # Add an empty cell to the row
        board_row.append("")

    # Add the row to the board
    board.append(board_row)

# current_turn will track whose turn it is ('X' or 'O'),
# game_over will indicate if the game has ended.
current_turn = "X"
game_over = False

# Function to draw the board
def draw_board():
    clear()
    set_stroke_color(1, 0, 0)  # color for the grid
    set_stroke_width(4)

    # Draw grid lines
    for i in range(1, BOARD_SZ):
        draw_line(i * CELL_SIZE, 0, i * CELL_SIZE, HEIGHT)
        draw_line(0, i * CELL_SIZE, WIDTH, i * CELL_SIZE)

    # Draw X's and O's
    for row in range(BOARD_SZ):
        for col in range(BOARD_SZ):
            centerX = col * CELL_SIZE + CELL_SIZE // 2
            centerY = row * CELL_SIZE + CELL_SIZE // 2

            # Draw an X if the cell contains 'X'
            if board[row][col] == "X":
                draw_x(centerX, centerY)
            # Draw an O if the cell contains 'O'
            elif board[row][col] == "O":
                draw_o(centerX, centerY)

# Function to draw X
def draw_x(x, y):
    # This function draws an X at the specified coordinates.
    offset = CELL_SIZE // 4
    draw_line(x - offset, y - offset, x + offset, y + offset)
    draw_line(x + offset, y - offset, x - offset, y + offset)

# Function to draw O
def draw_o(x, y):
    # This function draws an O at the specified coordinates.
    draw_circle(x, y, CELL_SIZE // 4)

# Function to handle mouse clicks
def handle_click(mx, my):
    # handles mouse clicks
    global current_turn, game_over

    if game_over:
        restart_game() # restart if over
        return

    # Determine the row and column that was clicked.
    row = my // CELL_SIZE
    column = mx // CELL_SIZE

    # If the clicked cell is empty, mark it with the current player's symbol.
    if board[row][column] == "":
        board[row][column] = current_turn

        # Check the game state (win, lose, or continue).
        if check_game_state():
            game_over = True
        else:
            # switch
            current_turn = "O" if current_turn == "X" else "X"

# Function to check for win or tie
def check_game_state():
    global winner

    # Check rows and columns for a win
    for i in range(BOARD_SZ):
        if board[i][0] == board[i][1] == board[i][2] != "":
            winner = board[i][0]
            return True
        if board[0][i] == board[1][i] == board[2][i] != "":
            winner = board[0][i]
            return True

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] != "":
        winner = board[0][0]
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        winner = board[0][2]
        return True

    # Check for tie (if no empty cells left)
    tie = True  # Assume it's a tie until an empty cell is found
    for row in range(BOARD_SZ):
        for col in range(BOARD_SZ):
            if board[row][col] == "":
                # Found an empty cell, so it's not a tie
                tie = False
                break  # No need to check further

        if not tie:
            break  # Break outer loop if an empty cell is found
    if tie:
        winner = None
        return True
    return False
# Function to draw the start screen
def draw_start_screen():
    clear()
    set_font_size(24)
    draw_text("Press 'P' to play Tic-Tac-Toe", WIDTH // 2 - 150, HEIGHT // 2)

# Function to draw the end screen
def draw_end_screen():
    clear()
    set_font_size(24)
    result_message = "It's a tie!" if winner is None else "Player " + str(winner) + " wins!"
    draw_text(result_message, WIDTH // 2 - 100, HEIGHT // 2)

# Function to draw the game
def draw_game():
    if not game_started:
        draw_start_screen()
    elif game_over:
        draw_end_screen()
    else:
        draw_board()

# Function to handle key presses
def handle_key_press(key):
    global game_started, game_over
    if key == "p" and not game_started:
        game_started = True
    elif game_over:
        restart_game()

# Modify the handle_click function
def handle_click(mx, my):
    global current_turn, game_over, winner, game_started

    if not game_started or game_over:
        return

    row = my // CELL_SIZE
    col = mx // CELL_SIZE

    if board[row][col] == "":
        board[row][col] = current_turn
        if check_game_state():
            game_over = True
        else:
            current_turn = "O" if current_turn == "X" else "X"

# Function to restart the game
def restart_game():
    global board, current_turn, game_over, winner, game_started
    board = []

    for i in range(BOARD_SZ):
        row = []
        for j in range(BOARD_SZ):
            row.append("")
        board.append(row)

    current_turn = "X"
    game_over = False
    winner = None
    game_started = False

# Start the graphics loop with key press handler
start_graphics(draw_game, mouse_press=handle_click, key_press=handle_key_press, width=WIDTH, height=HEIGHT)