import os

board = [' '] * 9
game_over = False
player = 'X'

def display_board():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('  ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('-----------')
    print('  ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('-----------')
    print('  ' + board[6] + ' | ' + board[7] + ' | ' + board[8])

def is_winner(p):
    return ((board[0] == p and board[1] == p and board[2] == p) or
            (board[3] == p and board[4] == p and board[5] == p) or
            (board[6] == p and board[7] == p and board[8] == p) or
            (board[0] == p and board[3] == p and board[6] == p) or
            (board[1] == p and board[4] == p and board[7] == p) or
            (board[2] == p and board[5] == p and board[8] == p) or
            (board[0] == p and board[4] == p and board[8] == p) or
            (board[2] == p and board[4] == p and board[6] == p))

def is_board_full():
    return ' ' not in board

while not game_over:
    display_board()
    choice = int(input('Escolha uma posição (1-9): ').strip())
    if board[choice-1] == ' ':
        board[choice-1] = player
        if is_winner(player):
            display_board()
            print(f'{player} venceu!')
            game_over = True
        elif is_board_full():
            display_board()
            print('Empate!')
            game_over = True
        else:
            player = 'O' if player == 'X' else 'X'
    else:
        print('Essa posição já está ocupada. Escolha outra.')

replay = input('Quer jogar novamente? (S/N) ').strip()
if replay.lower() == 's':
    board = [' '] * 9
    game_over = False
    player = 'X'
else:
    print('Até a próxima!')