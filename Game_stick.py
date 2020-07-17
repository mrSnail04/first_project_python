number=int(input('Введите количество палочек\n'))
p1=input('Имя первого игрока\n')
p2=input('Имя второго игрокa\n')
player_turn = p1
def can_take_stick(sticks):
    return sticks >= 1 and sticks <=3
def switch_players (turn):
    return p1 if player_turn == p2 else p2
def end_of_game(sticks):
    return number <=0

while (not end_of_game(number)):
    print(f'{player_turn}, сколько палочек хотите взять? Осталось {number}\n')
    taken=int(input())
    
    if not can_take_stick(taken) :
        print('Не правильно количесвто палочек')
        continue
    if number == 2 and taken == 3:
        print (f'{player_turn}, нельзя взять больше {number} палочек')
        continue
    if number == 1 and taken > 1:
        print (f'{player_turn}, нельзя взять больше {number} палочек')
        continue
    number -= taken
    print(f'{player_turn} взял {taken} палочек\n')
    
    if end_of_game(number):
        print(f'{player_turn} проиграл')
        break
    player_turn =switch_players(player_turn)