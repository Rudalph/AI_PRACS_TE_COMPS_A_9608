import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def brute_force_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    random.shuffle(players)

    print("Initial Board:")
    print_board(board)

    for _ in range(9):
        player = players[0]
        players.reverse()

        empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
        move = random.choice(empty_cells)
        board[move[0]][move[1]] = player

        print(f"\n{player}'s Move:")
        print_board(board)

        if check_winner(board, player):
            print(f"\n{player} wins!")
            break
        elif is_board_full(board):
            print("\nIt's a tie!")
            break

brute_force_tic_tac_toe()
