def print_board(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])
    print()


def check_winner(board):
    winning_lines = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]

    for a, b, c in winning_lines:
        if board[a] != " " and board[a] == board[b] and board[b] == board[c]:
            return board[a]

    return None


def check_draw(board):
    return " " not in board


def get_move(board, player):
    while True:
        try:
            move_text = input(f"Player {player}, enter a position (1-9): ").strip()
            move = int(move_text)
        except ValueError:
            print("Please enter a number from 1 to 9.")
            continue

        if move < 1 or move > 9:
            print("Please choose a number from 1 to 9.")
        else:
            index = move - 1
            if board[index] != " ":
                print("That square is already taken.")
            else:
                return index


def switch_player(player):
    return "O" if player == "X" else "X"


def play_game():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    player = "X"

    while True:
        print_board(board)

        move = get_move(board, player)
        board[move] = player

        winner = check_winner(board)
        if winner is not None:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("The game is a draw.")
            break

        player = switch_player(player)


if __name__ == "__main__":
    play_game()
