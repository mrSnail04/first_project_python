import random
shuld_continue= True
while shuld_continue:
    player = input('R/S/P').lower()
    if player not in ['r','s','p']:
        print('Incorrect input')
        continue
    gen = {1:'r', 2:'s', 3:'p'}
    comp=gen[random.randint(1,3)]
    winning_comb=[('p','r'),('r','s'),('s','p')]
    if player==comp:
        print('a draw')
    elif (player,comp) in winning_comb:
        print('Player wins')
    else:
    
        print('comp wins')
    shuld_continue = input('[y/n]')=='y'