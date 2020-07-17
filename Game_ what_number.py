import random
tries = 0
number = random.randint(1,50)
while tries<6:
    f = int(input('Enter the number\n'))
    tries+=1
    print(f'Your number is {f}')
    if number == f:
        print('Win')
        break
    if number < f:
        print('Number is less')
    if number > f:
        print ('Number is greater')
    if f != number and tries ==6:
        print(f'You lose, my number is {number}')
        break
