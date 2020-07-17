import random
shuld_continue= True
while shuld_continue:
    player = input('R/S/P\n').lower()
    if player not in ['r','s','p']:
        print('Incorrect input')
        continue
    gen = {1:'r', 2:'s', 3:'p'}
    comp=gen[random.randint(1,3)]
    winning_comb=[('p','r'),('r','s'),('s','p')]
    if player==comp:
        print('a draw')
    elif (player,comp) in winning_comb:
        print('You won')
    else:
        print('Computer won')
    shuld_continue = input('[y/n]\n')=='y'