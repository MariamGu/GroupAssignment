# Task 1
n = int(input("Enter the number or rows: "))
m = int(input("Enter the number of columns: "))

sequence = []

for i in range(n + 1):
    row = []
    for j in range(m + 1):
        if i == 0:
            row.append(j)
        elif j == 0:
            row.append(i)
        else:
            row.append(i * j)
    sequence.append(row)

for row in sequence:
    print(row)

# Task 2 - ვერ გავიგე

game_state = [["", "", ""], ["", "", ""], ["", "", ""]]

current_player = 'X'

for turn in range(9):
    for row in game_state:
        for cell in row:
            print(cell if cell else ' ', end=' | ')
        print("\n" + "-" * 9)

    valid_input = False
    while not valid_input:
        row_move = input(f"Player {current_player}, enter row index, column index, symbol (e.g., '0,1,X'): ")
        row_move_params = row_move.split(",")
        if len(row_move_params) == 3:
            row_index = int(row_move_params[0])
            column_index = int(row_move_params[1])
            symbol = row_move_params[2].upper()

            if symbol == current_player and 0 <= row_index < 3 and 0 <= column_index < 3:
                if game_state[row_index][column_index] == "":
                    game_state[row_index][column_index] = symbol
                    valid_input = True
                else:
                    print("That spot is taken. Try again.")
            else:
                print("Invalid input. Make sure to follow the format and use the correct symbol. If previously "
                      "entered X, enter O and vice versa.")

    winner = None
    for i in range(3):
        if game_state[i][0] != "" and game_state[i][0] == game_state[i][1] == game_state[i][2]:
            winner = game_state[i][0]
        if game_state[0][i] != "" and game_state[0][i] == game_state[1][i] == game_state[2][i]:
            winner = game_state[0][i]

    if game_state[0][0] != "" and game_state[0][0] == game_state[1][1] == game_state[2][2]:
        winner = game_state[0][0]
    if game_state[0][2] != "" and game_state[0][2] == game_state[1][1] == game_state[2][0]:
        winner = game_state[0][2]

    if winner:
        print(f"Player {winner} wins!")
        break

    is_draw = True
    for row in game_state:
        if "" in row:
            is_draw = False
            break
    if is_draw:
        print("The game is a draw!")
        break

    current_player = 'O' if current_player == 'X' else 'X'

for row in game_state:
    for cell in row:
        print(cell if cell else ' ', end=' | ')
    print("\n" + "-" * 9)