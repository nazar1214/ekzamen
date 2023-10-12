def pole(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def win(board, player):
    for row in board:
        row_cow = 0
        for cell in row:
            if cell == player:
                row_cow += 1
        if row_cow == 3:
            print(f"гравець {player} виграв!")
            return True

    for col in range(3):
        col_cow = 0
        for row in range(3):
            if board[row][col] == player:
                col_cow += 1
        if col_cow == 3:
            print(f"гравець {player} виграв!")
            return True

    dia1 = 0
    dia2 = 0
    for i in range(3):
        if board[i][i] == player:
            dia1 += 1
        if board[i][2 - i] == player:
            dia2 += 1
    if dia1 == 3 or dia2 == 3:
        print(f"гравець {player} виграв!")
        return True

def draw(board):
    for row in board:
        if " " in row:
            return False
    print("гра закінчилася нічиею.")
    return True

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    playerrn = "X"
    game_over = False

    while not game_over:
        pole(board)
        user_input = input(f"гравець {playerrn}, введіть стовпець і ряд (наприклад, '1 2'): ")
        if ' ' not in user_input:
            print(" добав пробіл між стовпцем і рядо")
            continue

        row, col = map(int, user_input.split())
        if row < 1 or row > 3 or col < 1 or col > 3:
            print("Введіть значення від 1 до 3")
            continue

        if board[row - 1][col - 1] == " ":
            board[row - 1][col - 1] = playerrn
            if win(board, playerrn) or draw(board):
                pole(board)
                game_over = True
            else:
                playerrn = "O" if playerrn == "X" else "X"
        else:
            print("Ця клітинка вже зайнята")

play_game()

