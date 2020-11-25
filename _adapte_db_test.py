import psycopg2
from psycopg2.extras import execute_values, RealDictCursor

conn = psycopg2.connect(dbname='testdb', user='postgres', password='Vfrcbv04')
cur = conn.cursor() #Создаём курсор
cur.execute('DROP TABLE IF EXISTS superheroes')
cur.execute('DROP TABLE IF EXISTS traffic_light')
conn.commit() # Передаём, для выполнения кода
cur.execute("CREATE TABLE superheroes(hero_id serial PRIMARY KEY, hero_name varchar, strength int);")
cur.execute("INSERT INTO superheroes(hero_name, strength) VALUES (%s, %s)", ('Superman', 100)) # вносим новые данные, только таким образом
cur.execute("""
            INSERT INTO superheroes(hero_name, strength)
            VALUES(%(name)s, %(strength)s);
            """, {'name':'Green Arrow', 'strength':80})
cur.execute("""
            INSERT INTO superheroes(hero_name, strength)
            VALUES(%(name)s, %(strength)s);
            """, {'name':'Flash', 'strength':999})

conn.commit()
cur.execute('CREATE TABLE traffic_light (light_id serial PRIMARY KEY, light text);')
#cur.execute('INSERT INTO traffic_light(light) VALUES ('%s')',(10))
#такой ввод не допускается. %s не брать в ковычки
#Если передаёшь один аргумент, то в конце ставить "," (10,)
cur.execute('INSERT INTO traffic_light(light) VALUES (%s)',('red',))
conn.commit()
cur.execute('SELECT * FROM superheroes')
one_line= cur.fetchone() #Вывод одной записи из таблицы
print(one_line)

full_fetch = cur.fetchall()#Вывод всех данных из таблицы
for record in full_fetch:
    print(record)

conn.commit()
cur.close()#закрываем курсор
conn.close()#закрываем конекшен
try:
    with psycopg2.connect(dbname='testdb', user='postgres', password='Vfrcbv04') as conn:
        with conn.cursor(cursor_factory = RealDictCursor) as curs:
            execute_values(curs, 'INSERT INTO traffic_light (light) VALUES %s',[('green',),('yellow',)])

            curs.execute('SELECT * FROM traffic_light')
            records = curs.fetchall()
            print(records)
            print(records[0]['light'])
finally:
    conn.close()
#после выхода из with connect не закрывается. закрывается cursor, и транзакции.

