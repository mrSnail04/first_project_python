import random
tries = 0
number = random.randint(1,50)
while tries<6:
    f = int(input('Enter the number\n'))
    tries+=1
    if number == f:
        print('win')
        break
    if number < f:
        print('number is less')
    if number > f:
        print ('number is greater')
    if f != number and tries ==6:
        print(f'You lose, my number is {number}')
        break
