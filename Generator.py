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


# итераторы
iterable = [1,2,3]

iterator = iter(iterable)
print(type(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

import itertools as it

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)
even_numbers = it.count(0,2)
print(even_numbers)

#for x in even_numbers:   Будет бесконечый цикл
#   print(x)
#Что бы этого избежать используют list

print(list(next(even_numbers) for _ in range(5)))

print(list(zip(it.count(),['a','b','c'])))

def print_iterable(iterable, end = None):
    for x in iterable:
        if end:
            print(x, end = end)
        else:
            print(x)
ones = it.repeat(1,5)
print_iterable(ones, ' ')

print(  list(map(pow, range(10), it.repeat(2))))

pos_neg_ones = it.cycle([1, -1])
print(list(next(pos_neg_ones) for _ in range(3)))

letters = it.cycle(['A','B','C'])
print(list(next(letters) for _ in range(10)))

print(list(it.accumulate([1,2,3,4,5])))
print(list(it.accumulate(['A','B','C','D'])))
print(list(it.accumulate([3,1,5,8,2,1,9,4,51,0,-1], max)))
# идёт сравнение. первое значение просто выводится, а дальше 3:1=3,3:5=5,5:8=8,8:2=8,8:1=8,8:9=9 и т.д
# Вывод: [3, 3, 5, 8 ,8 ,8 9, 9, 51, 51, 51]

print(list(it.chain('ABC','DEF')))

print(list(it.chain.from_iterable(['ABC','DEF'])))
#удаляет из списка все True
print(list(it.dropwhile(lambda x: x<3, [1,2,3,4,5])))
#удаляет из списка все False
print(list(it.takewhile(lambda x: x<3, [1,2,3,4,5])))
#удаляет всё, что True
print(list(it.filterfalse(lambda x: x%2==0, range(10))))

names = ['Carls','Car','Mamb','Ding','Giri']
ratings = [2842,2584,5156,2484,7484]
for name, rating in zip(names, ratings):
    print(f'{name}:{rating}')

print(list(zip(names,ratings)))
print(dict(zip(names,ratings)))
#Cramnic просто выкидывается раз нету rating
names = ['Carls','Car','Mamb','Ding','Giri','Cramnic']
ratings = [2842,2584,5156,2484,7484]
print(dict(zip(names,ratings)))
#zip_longest позволяет сохранить лишнее значение с None
print(dict(it.zip_longest(names,ratings)))

#groupby сортирует в вид key:[value,value,value], учитывает порядок следования эле-тов
for key, grp in it.groupby([1,1,1,2,2,2,3,3]):
    print('{}:{}'.format(key,list(grp)))
#обязательно передавать сгруппированный список, иначе работет не правильно
for key, grp in it.groupby([1,2,1,3,2,1,3,2]):
    print('{}:{}'.format(key,list(grp)))

lst = [1,2,1,3,2,1,3,2]
for key, grp in it.groupby(sorted(lst)):
    print('{}:{}'.format(key,list(grp)))
#groupby к словарям
forecast = [{'humidity' : 20, 'temperature' : 78, 'wind' : 7},
            {'humidity' : 50, 'temperature' : 61, 'wind' : 10},
            {'humidity' : 100, 'temperature' : 81, 'wind' : 5},
            {'humidity' : 90, 'temperature' : 62, 'wind' : 15},
            {'humidity' : 20, 'temperature' : 84, 'wind' : 19},
            {'humidity' : 0, 'temperature' : 66, 'wind' : 28},
            {'humidity' : 100, 'temperature' : 87, 'wind' : 12},
            {'humidity' : 0, 'temperature' : 68, 'wind' : 14},
            {'humidity' : 90, 'temperature' : 86, 'wind' : 4},
            {'humidity' : 50, 'temperature' : 68, 'wind' : 0}
            ]
def group_sorted (iterable, key=None):
    return it.groupby(sorted(iterable, key = key), key = key)
grouped_data = group_sorted(forecast, key=lambda x: x['humidity'])
for key, grp in grouped_data:
    print('{}:{}'.format(key, list(grp)))
