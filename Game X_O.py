
board=['','','','','','','','','']
def print_state(state):
    for i, v in enumerate(state):
        if (i+1)%3==0:
            print(f'{v}')
        else:
            print(f'{v}|',end='')
winer_combin = [(0,1,2),(3,4,5),(6,7,8),(0,4,8),(2,4,6),(0,3,6),(1,4,7),(2,5,8)]
def winer(state, combination):
    for (x, y, z) in combination:
        if state[x] == state[y] and state[y]==state[z] and (state[x]== 'X' or state[x]=='O'):
            return state[x]
        return ''
def play_game(board):
    current_sign='X'
    while(winer(board,winer_combin)==''):
        index = input('Введите индекс клетки\n')
        if index =='q':
            print('Выход из игры')
            break 
        if index != (0,1,2,3,4,5,6,7,8,'q'):
            print('Не правильное значение error\n')
        try:
            if int(index) > 8 or int(index) < 0:
                print('Не правильный индекс\n')
                continue
        except ValueError:
            print("Не правильное значение")
            continue
        board[int(index)] = current_sign
        print_state(board)
        winner_sign = winer(board, winer_combin)
        if winner_sign !='':
            print(f'{winner_sign} win')
            current_sign = 'X' if current_sign =='O' else 'O'
play_game(board)