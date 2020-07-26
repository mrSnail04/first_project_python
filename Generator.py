#Урок генераторы.
#По генератору можно пройтись только один раз. 
#Если надо пройтись несколько раз, лучше использовать lst
import random
import itertools

def randoms(min, max, n):
    for i in range(n):
        yield random.randint(min, max)

for r in randoms(10, 30, 5):
    print(r)

rand = randoms(1,10,10)
print(rand)
seq = list(randoms(1,10,5))
print(seq)
#При помощи itertools можно взять меньше значений, чем сгенерированно 
rand_seq = randoms(1,10,10) #генерировать 10 штуку
five_take = list(itertools.islice(rand_seq, 5)) #требуется взять 5 значений
print(five_take)


def rando(min,max):
    while True:
        yield random.randint(min, max)
#при помощи next() можно возвращать следующее значение
rand_seq = rando(1,10)
n=next(rand_seq)
print(n)
rand_seq = rando(1,10)
n=next(rand_seq)
print(n)
rand_seq = rando(1,10)
n=next(rand_seq)
print(n)
rand_seq = rando(1,10)
n=next(rand_seq)
print(n)

my_list = [1,2,3,4]

squares = [x**2 for x in my_list]
print(squares)

squares = (x**2 for x in my_list)
print(squares) #так же генератор 